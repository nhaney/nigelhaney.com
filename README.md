[![Netlify Status](https://api.netlify.com/api/v1/badges/1b7350d9-533f-45c4-a699-39a35e98e87f/deploy-status)](https://app.netlify.com/sites/lucid-ride-8b31a8/deploys)

# Source of `nigelhaney.com`

Developed with Tailwind CSS and Vanilla Javascript and a custom python static site generator.

# portfolio-generator

`portfolio-generator` is a simple static site generator that will take a configuration file
`portfolio.json` and the name of the a source directory and will statically generate a site based on 
the configuration file. 

Example usage:

`portfolio.json`
```json
{
    // resources have a name which will be formatted like: <resource name>-<uuid>.<resource extension> in the 
    // final build. This is to prevent web browser caching of previous versions.
    "resources": [ 
        {
            "name": "resume.pdf", // will be generated as resume-5c7e1696.pdf
            "destination": "<resource path>", // path in built directory where this resource will be located. Defaults to `resources/`
            "resource_type": "googledoc", // there are different types of resources that will be pluggable to the generator
            "info": { // info is extra data needed to get the google doc
                "document_id": <google doc id>
            }
        }
    ],
    // bundles are like resources, but include multiple files in an archive. 
    // All of the files extracted are appended a uuid as well to prevent caching between versions
    "bundles": [
        {
            "destination": "destination/directory/",
            archive_type": "zip" // eventually support .tar, .gz as well,
            "resource_type": "github_actions_artifact",
            "info": {
                "repo": "nhaney/fish-game",
                "artifact_regex": ".*-WASM-.*" // regex that will match the artifact name
            }
        }
    ],
    "profile": { // optional key value data that can be used to fill out a portfolio / about me page
        "job": {
            "title": "my job title",
            "employer": "my employer",
            "employer_link": "myemployer.com"
        },
        "interests": [
            {
                "description": "this is an interest of mine",
                "link": null,
            },
            {
                "description": "this is another interest of mine",
                "link": "interests.com#mysecondinterest"
            }
        ],
        "social_links": {
            "github_url": "https://github.com/nhaney",
            "linkedin_url": "https://linkedin.com/in/nigel-haney",
            "email": "nigel.haney27@gmail.com"
        }
    },
    "extra": { // any extra key value data that is needed can go here
        "extra": "data"
    }
}
```

Example of templated html using the above config (uses Jinja2 templating):

```html
<!doctype html>
<html lang="en">
<body>
    <h1></h1>
</body>
</html>
```
