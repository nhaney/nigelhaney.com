# Goals for my website

* [x] Create nix flake for development shell that has dependencies that can build the site
* [ ] Create nix derivation that has the complete site in it. Site should be able to be built with `nix build`.
    * [ ] Move to tailwindcss cli since that is all that I use node for and install that instead.
* [ ] Create github action that builds the site using nix and deploys the site to cloudflare pages
* [ ] Create HTML/CSS resume and export to PDF
    * https://veerasundar.com/blog/how-to-make-resume-in-html-export-to-pdf
    * command: `chromium-browser --headless --disable-gpu --no-pdf-header-footer --print-to-pdf-no-header  --print-to-pdf=file1.pdf http://www.example.com`

