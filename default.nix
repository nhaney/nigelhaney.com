{ stdenv, tailwindcss }:
stdenv.mkDerivation {
    pname = "nigelhaney.com";
    version = "1.0.0";
    src = ./.;

    nativeBuildInputs = [
        tailwindcss
    ];

    buildPhase = ''
        tailwindcss -i css/styles.css -c css/tailwind.config.js --output public/css/tailwind.css
    '';

    installPhase = ''
        mkdir -p $out
        cp -rf ./public $out
    '';
}
