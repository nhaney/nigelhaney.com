{ stdenv, python3, chromium, makeFontsConf, noto-fonts-emoji, fira-code, dejavu_fonts }:
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

        # Copy fonts to resources in order to self-host fonts.
        mkdir -p $out/resources/fonts

        #cp ${fira-code}/share/fonts/truetype/FiraCode-VF.ttf $out/resources/fonts/fira-code.ttf

        #cp ${dejavu_fonts}/share/fonts/truetype/DejaVuSans.ttf $out/resources/fonts/dejavu-sans.ttf
        #cp ${dejavu_fonts}/share/fonts/truetype/DejaVuSans-Bold.ttf $out/resources/fonts/dejavu-sans-bold.ttf
        #cp ${dejavu_fonts}/share/fonts/truetype/DejaVuSans-Oblique.ttf $out/resources/fonts/dejavu-sans-italic.ttf

        ## TODO: See if we can reduce the size of this by only including emojis we need.
        #cp ${noto-fonts-emoji}/share/fonts/noto/NotoColorEmoji.ttf $out/resources/fonts/noto-color-emoji.ttf

        # Use chrome to create PDF of resume.
        chromium-browser --no-sandbox --headless --no-margins --no-pdf-header-footer --print-to-pdf-no-header --run-all-compositor-stages-before-draw --print-to-pdf=$out/resources/resume.pdf $out/resume/index.html
    '';
}
