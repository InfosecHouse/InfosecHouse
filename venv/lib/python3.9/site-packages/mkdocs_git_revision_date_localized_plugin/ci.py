"""
Helper functions related to continuous integration (CI).

This is because often CI runners do not have access to full git history.
"""

import os
import logging


def raise_ci_warnings(repo) -> None:
    """
    Raise warnings when users use plugin on CI build runners.

    Args:
        repo (GitPython.git.repo): The Git repo object.
    """
    if not is_shallow_clone(repo):
        return None

    n_commits = commit_count(repo)


    # Gitlab Runners
    if os.getenv("GITLAB_CI") is not None and n_commits < 50:
        # Default is GIT_DEPTH of 50 for gitlab
        logging.warning(
            """
                [git-revision-date-localized-plugin] Running on a GitLab runner might lead to wrong
                Git revision dates due to a shallow git fetch depth.

                Make sure to set GIT_DEPTH to 0 in your .gitlab-ci.yml file
                (see https://docs.gitlab.com/ee/user/project/pipelines/settings.html#git-shallow-clone).
                """
        )

    # Github Actions
    elif os.getenv("GITHUB_ACTIONS") is not None and n_commits == 1:
        # Default is fetch-depth of 1 for github actions
        logging.warning(
            """
                [git-revision-date-localized-plugin] Running on GitHub Actions might lead to wrong
                Git revision dates due to a shallow git fetch depth.

                Try setting fetch-depth to 0 in your GitHub Action
                (see https://github.com/actions/checkout).
                """
        )

    # Azure Devops Pipeline
    # Does not limit fetch-depth by default
    elif int(os.getenv("Agent.Source.Git.ShallowFetchDepth", 10e99)) < n_commits:
        logging.warning(
            """
                [git-revision-date-localized-plugin] Running on Azure pipelines with limited
                fetch-depth might lead to wrong git revision dates due to a shallow git fetch depth.

                Remove any Shallow Fetch settings
                (see https://docs.microsoft.com/en-us/azure/devops/pipelines/repos/pipeline-options-for-git?view=azure-devops#shallow-fetch).
                """
        )

    # Bitbucket pipelines
    elif os.getenv("CI") is not None and n_commits < 50:
        # Default is fetch-depth of 50 for bitbucket pipelines
        logging.warning(
            """
                [git-revision-date-localized-plugin] Running on bitbucket pipelines might lead to wrong
                Git revision dates due to a shallow git fetch depth.

                Try setting "clone: depth" to "full" in your pipeline
                (see https://support.atlassian.com/bitbucket-cloud/docs/configure-bitbucket-pipelinesyml/
                and search 'depth').
                """
        )



def commit_count(repo) -> int:
    """
    Determine the number of commits in a repository.

    Args:
        repo (GitPython.Repo.git): Repository.

    Returns:
        count (int): Number of commits.
    """
    return int(repo.rev_list('--count','HEAD'))


def is_shallow_clone(repo) -> bool:
    """
    Determine if repository is a shallow clone.

    References & Context:
    https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/issues/10
    https://stackoverflow.com/a/37203240/5525118

    Args:
        repo (GitPython.Repo.git): Repository

    Returns:
        bool: If a repo is shallow clone
    """
    return os.path.exists(".git/shallow")
