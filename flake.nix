{
  description = "Flake containing build environment for nigelhaney.com";

  inputs = {
    nixpkgs = {
      url = "nixpkgs/nixos-unstable";
    };
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
    fish-game = {
        url = "git+https://github.com/nhaney/fish-game?ref=update-bevy-version&rev=2867172ed8323ba0dac63cb7e8de7b5da2581e5f";
    };
  };

  outputs = { nixpkgs, flake-utils, fish-game, ... }:
    flake-utils.lib.eachDefaultSystem(system:
      let
        pkgs = import nixpkgs { inherit system; overlays = [ (final: prev: { fish-game = fish-game.packages.${system}.wasm; })]; };
      in
      {
        packages = {
          default = pkgs.callPackage ./default.nix {};
        };
        devShells.default = pkgs.mkShellNoCC {
          packages = with pkgs; [
            # Used for styling the website.
            tailwindcss
            # Used for static site generation and local site hosting
            python3
            # Used for print to pdf functionality
            chromium
            # Used for running build commands for project.
            just
            # Used for live server.
            nodePackages.live-server
          ];
        };
      }
    );
}
