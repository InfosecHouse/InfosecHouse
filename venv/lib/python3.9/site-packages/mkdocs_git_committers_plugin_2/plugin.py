import os
import sys
import logging
from pprint import pprint
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

from git import Repo, Commit
import requests, json
from requests.exceptions import HTTPError
import time
import hashlib
import re
from bs4 import BeautifulSoup as bs

LOG = logging.getLogger("mkdocs.plugins." + __name__)

class GitCommittersPlugin(BasePlugin):

    config_scheme = (
        ('enterprise_hostname', config_options.Type(str, default='')),
        ('repository', config_options.Type(str, default='')),
        ('branch', config_options.Type(str, default='master')),
        ('docs_path', config_options.Type(str, default='docs/')),
        ('enabled', config_options.Type(bool, default=True)),
        ('cache_dir', config_options.Type(str, default='.cache/plugin/git-committers')),
        ('token', config_options.Type(str, default='')),
    )

    def __init__(self):
        self.total_time = 0
        self.branch = 'master'
        self.enabled = True
        self.authors = dict()
        self.cache_page_authors = dict()
        self.cache_date = ''

    def on_config(self, config):
        self.enabled = self.config['enabled']
        if not self.enabled:
            LOG.info("git-committers plugin DISABLED")
            return config

        LOG.info("git-committers plugin ENABLED")

        if not self.config['token'] and 'MKDOCS_GIT_COMMITTERS_TOKEN' in os.environ:
            self.config['token'] = os.environ['MKDOCS_GIT_COMMITTERS_TOKEN']

        if not self.config['repository']:
            LOG.error("git-committers plugin: repository not specified")
            return config
        if self.config['enterprise_hostname'] and self.config['enterprise_hostname'] != '':
            self.githuburl = "https://" + self.config['enterprise_hostname'] + "/"
        else:
            self.githuburl = "https://github.com/"
        self.localrepo = Repo(".")
        self.branch = self.config['branch']
        return config

    def list_contributors(self, path):
        last_commit_date = ""
        path = path.replace("\\", "/")
        for c in Commit.iter_items(self.localrepo, self.localrepo.head, path):
            if not last_commit_date:
                # Use the last commit and get the date
                last_commit_date = time.strftime("%Y-%m-%d", time.gmtime(c.authored_date))

        # File not committed yet
        if last_commit_date == "":
            last_commit_date = datetime.now().strftime("%Y-%m-%d")
            return [], last_commit_date

        # Try to leverage the cache
        if path in self.cache_page_authors:
            if self.cache_date and time.strptime(last_commit_date, "%Y-%m-%d") < time.strptime(self.cache_date, "%Y-%m-%d"):
                return self.cache_page_authors[path]['authors'], self.cache_page_authors[path]['last_commit_date']

        url_contribs = self.githuburl + self.config['repository'] + "/contributors-list/" + self.config['branch'] + "/" + path
        LOG.info("git-committers: fetching contributors for " + path)
        LOG.debug("   from " + url_contribs)
        authors=[]
        headers = {}
        if self.config['token'] and self.config['token'] != '':
            headers = {'Authorization': 'token ' + self.config['token']} 

        try:
            response = requests.get(url_contribs, headers=headers)
            response.raise_for_status()
        except HTTPError as http_err:
            LOG.error(f'git-committers: HTTP error occurred: {http_err}\n(404 is normal if file is not on GitHub yet or Git submodule)')
        except Exception as err:
            LOG.error(f'git-committers: Other error occurred: {err}')
        else:
            html = response.text
            # Parse the HTML
            soup = bs(html, "lxml")
            lis = soup.find_all('li')
            for li in lis:
                a_tags = li.find_all('a')
                login = a_tags[0]['href'].replace("/", "")
                url = self.githuburl + login
                name = login
                img_tags = li.find_all('img')
                avatar = img_tags[0]['src']
                avatar = re.sub(r'\?.*$', '', avatar)
                authors.append({'login':login, 'name': name, 'url': url, 'avatar': avatar})
            # Update global cache_page_authors
            self.cache_page_authors[path] = {'last_commit_date': last_commit_date, 'authors': authors}

        return authors, last_commit_date

    def on_page_context(self, context, page, config, nav):
        context['committers'] = []
        if not self.enabled:
            return context
        start = timer()
        git_path = self.config['docs_path'] + page.file.src_path
        authors, last_commit_date = self.list_contributors(git_path)
        if authors:
            context['committers'] = authors
        if last_commit_date:
            context['last_commit_date'] = last_commit_date
        end = timer()
        self.total_time += (end - start)

        return context

    def on_post_build(self, config):
        LOG.info("git-committers: saving page authors cache file")
        json_data = json.dumps({'cache_date': datetime.now().strftime("%Y-%m-%d"), 'page_authors': self.cache_page_authors})
        os.makedirs(self.config['cache_dir'], exist_ok=True)
        f = open(self.config['cache_dir'] + "/page-authors.json", "w")
        f.write(json_data)
        f.close()

    def on_pre_build(self, config):
        if os.path.exists(self.config['cache_dir'] + "/page-authors.json"):
            LOG.info("git-committers: found page authors cache file - loading it")
            f = open(self.config['cache_dir'] + "/page-authors.json", "r")
            cache = json.loads(f.read())
            self.cache_date = cache['cache_date']
            self.cache_page_authors = cache['page_authors']
            f.close()
