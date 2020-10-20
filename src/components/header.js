import { Link } from "gatsby"
import PropTypes from "prop-types"
import React from "react"
import { Styled } from "theme-ui"

const Header = ({ siteTitle }) => (
  <header
    style={{
      marginBottom: `1.45rem`,
    }}
  >
    <div
      style={{
        margin: `0 auto`,
        maxWidth: 960,
        padding: `1.45rem 1.0875rem`,
        borderBottom: `1px solid`,
        borderImage: `linear-gradient(45deg, black, white) 1`,
      }}
    >
      <Styled.h1 style={{ margin: 0 }}>
        <Link
          to="/"
          style={{
            textDecoration: `none`,
            color: `black`,
          }}
        >
          {siteTitle}
        </Link>
      </Styled.h1>
    </div>
  </header>
)

Header.propTypes = {
  siteTitle: PropTypes.string,
}

Header.defaultProps = {
  siteTitle: ``,
}

export default Header
