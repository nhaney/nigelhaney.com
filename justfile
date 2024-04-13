set shell := [ "bash", "-c" ]

build-site:
    cp -rf src public

# TODO: Figure out how to either make a shebang bash script with nix or make this kill the server more accurately (temp file maybe?)
build-resume: build-site
    python -m http.server -d public/ &
    chromium-browser --headless --no-margins --no-pdf-header-footer --print-to-pdf-no-header --run-all-compositor-stages-before-draw --print-to-pdf=./public/resources/resume.pdf http://127.0.0.1:8000/resume/
    kill $(ps aux | grep -v "grep" | grep "python -m http.server" | awk '{ print $2 }')

