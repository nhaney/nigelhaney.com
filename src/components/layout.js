import "fontsource-source-code-pro"
import React from "react"
import PropTypes from "prop-types"
import { useStaticQuery, graphql } from "gatsby"

import Footer from "./footer"
import Header from "./header"

const Layout = ({ children }) => {
  const data = useStaticQuery(graphql`
    query SiteTitleQuery {
      site {
        siteMetadata {
          title
          socialLinks {
            url
            type
          }
        }
      }
    }
  `)

  return (
    <div
      style={{
        display: `flex`,
        minHeight: `100vh`,
        flexDirection: `column`,
      }}
    >
      <Header siteTitle={data.site.siteMetadata?.title || `Title`} />
      <div
        style={{
          margin: `0 auto`,
          maxWidth: 960,
          padding: `0 1.0875rem 1.45rem`,
          flex: `1`,
        }}
      >
        <main>{children}</main>
      </div>
      <Footer socialLinks={data.site.siteMetadata.socialLinks} />
    </div>
  )
}

Layout.propTypes = {
  children: PropTypes.node.isRequired,
}

export default Layout
