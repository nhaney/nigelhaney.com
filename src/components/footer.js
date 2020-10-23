import PropTypes from "prop-types"
import React from "react"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faQuestion } from "@fortawesome/free-solid-svg-icons"
import { faGithub, faLinkedin } from "@fortawesome/free-brands-svg-icons"

const SocialLink = ({ url, icon, alt }) => (
  <div>
    <a
      href={url}
      style={{ color: `black`, fontSize: `1.5rem`, fontWeight: 600 }}
    >
      <FontAwesomeIcon icon={icon} alt={alt} />
    </a>
  </div>
)

SocialLink.propTypes = {
  url: PropTypes.string,
  alt: PropTypes.string,
  icon: PropTypes.any,
}

const SocialDivider = () => (
  <div
    style={{
      height: `100%`,
      borderLeft: `1px solid black`,
      marginRight: `20px`,
      marginLeft: `20px`,
    }}
  />
)

function generateSocialButton(socialLink) {
  const socialIconMap = {
    github: [faGithub, "My GitHub Profile"],
    linkedin: [faLinkedin, "My LinkedIn Profile"],
  }

  let icon = socialIconMap[socialLink.type]
  if (icon === undefined) {
    icon = [faQuestion, "Unknown Profile"]
  }

  return <SocialLink url={socialLink.url} icon={icon[0]} alt={icon[1]} />
}

const Footer = ({ socialLinks }) => {
  const footerIcons = []

  for (const socialLink of socialLinks.slice(0, -1)) {
    footerIcons.push(generateSocialButton(socialLink))
    footerIcons.push(<SocialDivider />)
  }
  footerIcons.push(generateSocialButton(socialLinks.slice(-1)[0]))

  return (
    <footer>
      <hr
        style={{
          border: `0`,
          height: `1px`,
          background: `linear-gradient(45deg, black, white)`,
          maxWidth: 960,
        }}
      />
      <div
        style={{
          maxWidth: 960,
          margin: `0 auto`,
          padding: `1.45rem 1.0875rem`,
          display: `flex`,
          flexDirection: `row`,
          justifyContent: `space-between`,
        }}
      >
        <div
          style={{
            display: `flex`,
            flexDirection: `row`,
          }}
        >
          {footerIcons}
        </div>
        <div
          style={{
            justifyContent: `flex-end`,
          }}
        >
          © {new Date().getFullYear()}, Source on {` `}
          <a href="https://github.com/nhaney/nigelhaney.com">Github.</a>
        </div>
      </div>
    </footer>
  )
}

Footer.propTypes = {
  socialLinks: PropTypes.arrayOf(PropTypes.object),
}

export default Footer
