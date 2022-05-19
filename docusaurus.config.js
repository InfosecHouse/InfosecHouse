// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Infosec House',
  tagline: 'Tools & Resources for Cyber Security Operations.',
  url: 'https://infosec.house',
  baseUrl: '/website',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.png',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'infosechouse', // Usually your GitHub org/user name.
  projectName: 'infosechouse', // Usually your repo name.

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Home',
        logo: {
          alt: 'My Site Logo',
          src: 'img/infosechouse.png',
        },
        items: [
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'Tools & Resources',
          },  
          {to: '/blog', label: 'Blog', position: 'left'},
          {
            href: 'https://github.com/infosechouse',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Community',
            items: [
              {
                label: 'Discord',
                href: 'https://discord.gg/2DHRCApSRa',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/InfosecHouse',
              },
              {
                label: 'Twitch',
                href: 'https://twitch.tv/InfosecHouse',
              },
              {
                label: 'Telegram',
                href: 'https://t.me/InfosecHouse',
              },
              {
                label: 'YouTube',
                href: 'https://www.youtube.com/channel/UC4PgsAu56TSpzH66aIOqbKQ',
              },
            ],
          },
          {
            title: 'Blog',
            items: [
              {
                label: 'Updates',
                to: '/blog/tags/updates',
              },
              {
                label: 'Offensive Security',
                to: '/blog/tags/offensive-security',
              },
              {
                label: 'Defensive Security',
                to: '/blog/tags/defensive-security',
              },
              {
                label: 'Operation Security',
                to: '/blog/tags/operation-security',
              },
              {
                label: 'Purple Security',
                to: '/blog/tags/purple-security',
              },
            ]
           },
          {
            title: 'Repositories',
            items: [
              {
                label: 'Infosec House',
                href: 'https://github.com/InfosecHouse/InfosecHouse',
              },
            ],
          },
        ],
        copyright: `© 2020-${new Date().getFullYear()} | Infosec House | Built with <a href="https://docusaurus.io/" target="_blank">🦖</a>`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = {
  url: 'https://infosechouse.netlify.app',
  baseUrl: '/website', 
  title: 'Infosec House'
};