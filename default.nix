{ stdenv, python3, chromium, makeFontsConf, noto-fonts-emoji, fira-code, dejavu_fonts }:
let 
    fontPkgsForChrome = [
        dejavu_fonts
        noto-fonts-emoji
        fira-code
    ];
in
stdenv.mkDerivation {
    pname = "nigelhaney.com";
    version = "1.0.0";
    src = ./src;

    nativeBuildInputs = [
        python3
        chromium
    ] ++ fontPkgsForChrome;

    # Chrome won't load any fonts by default, add a font config file so it does.
    FONTCONFIG_FILE = makeFontsConf {
        fontDirectories = fontPkgsForChrome;
    };

    buildPhase = ''
        # Prepare output directory
        mkdir -p $out

        # Copy html files from src to output directory
        cp -rf . $out/

        cp $FONTCONFIG_FILE $out/

        # Use chrome to create PDF of resume.
        python -m http.server -d $out &
        serverpid=$!
        chromium-browser --no-sandbox --headless --no-margins --no-pdf-header-footer --print-to-pdf-no-header --run-all-compositor-stages-before-draw --print-to-pdf=$out/resources/resume.pdf $out/resume/index.html
        kill $serverpid
    '';
}
