module.exports = {
  siteMetadata: {
    title: `Nigel Haney`,
    description: `Homepage of Nigel Haney`,
    author: `Nigel Haney`,
    socialLinks: [
      {
        type: `github`,
        url: `https://github.com/nhaney`,
      },
      {
        type: `linkedin`,
        url: `https://www.linkedin.com/in/nigel-haney/`,
      },
    ],
  },
  plugins: [
    `gatsby-plugin-react-helmet`,
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `assets`,
        path: `${__dirname}/src/assets`,
      },
    },
    "gatsby-plugin-theme-ui",
  ],
}
