{ stdenv, python3, chromium, makeFontsConf, noto-fonts-emoji, fira-code, dejavu_fonts, fish-game }:
let 
    fontPkgs = [
        dejavu_fonts
        fira-code
        noto-fonts-emoji
    ];
in
stdenv.mkDerivation {
    pname = "nigelhaney.com";
    version = "1";
    src = ./src;

    nativeBuildInputs = [
        python3
        chromium
    ] ++ fontPkgs;

    # Chrome won't load any fonts by default, add a font config file that loads the fonts we need when printing.
    FONTCONFIG_FILE = makeFontsConf {
        fontDirectories = fontPkgs;
    };

    buildPhase = ''
        # Prepare output directory
        mkdir -p $out

        # Copy html files from src to output directory
        cp -rf . $out/

        cp -rf ${fish-game}/bin/* $out/fish-game

        # Use chrome to create PDF of resume.
        chromium-browser --no-sandbox --headless --no-margins --no-pdf-header-footer --print-to-pdf-no-header --run-all-compositor-stages-before-draw --print-to-pdf=$out/resources/resume.pdf $out/resume/index.html
    '';
}
