[![Netlify Status](https://api.netlify.com/api/v1/badges/1b7350d9-533f-45c4-a699-39a35e98e87f/deploy-status)](https://app.netlify.com/sites/lucid-ride-8b31a8/deploys)

# Source of `nigelhaney.com`

Developed with Tailwind CSS and Vanilla Javascript and a custom python static site generator.

# portfolio-generator

`portfolio-generator` is a simple static site generator that will take a configuration file
`portfolio.json` and the name of the a source directory and will statically generate a site based on 
the configuration file.

The design goals of this generator are:
- Not to abstract away directory hierarchy of site
- Not to abstract away writing HTML
  - But allow for templating that HTML for reusability across pages
- Provide settings file that can be used to fill in basic information that is necessary (or at least I use)
  for a portfolio
- Allow resources to be fetched from arbitrary sources
  - New sources should be pluggable
  - Resources should be able to be placed anywhere in site directory hierarchy
  - Resources should optionally allow a unique identifier to be included on them to update browser caches 
    on updates
  - When building the site, throw an error by default if a resource is fetched but unused in any of the
    static files
- Able to build site from one command allowing for easy deployment on a platform like Netlify

## Current supported resource types

### Google doc export
- Fetch a google doc by ID and export it
  - Specify id in config file
  - Specify export type in config file (pdf, docx, etc.)
  - Pass in credentials through environment variables

### Github artifact
  - Fetch a github artifact
    - give a repo
    - optionally specify a regex for the artifact to pull
    - specify entry points that must be directly referred to in any of the templates
    - Pass in credentials through environment variables

