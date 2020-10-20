import React from "react"

import Layout from "../components/layout"
import SEO from "../components/seo"
import resume from "../assets/Nigel-Haney-Resume.pdf"

const IndexPage = () => {
  return (
    <Layout>
      <SEO title="Home" />
      <h1 title="General Kenobi">
        <span role="img" aria-label=":wave:">
          👋
        </span>
        Hello there!
      </h1>
      <p>
        I am a software developer primarily interested in backend web
        development and developer tools currently employed as a Software
        Engineer by <a href="https://www.parsons.com">Parsons Corporation</a>.
        You can find my resume <a href={resume}>here</a>.
        <br />
        <br />
        In my spare time outside of work I like to{" "}
        <a href="https://youtu.be/T4j9RSNbssU">speedrun video games</a>, learn
        about music production, and develop games.
      </p>
    </Layout>
  )
}

export default IndexPage
