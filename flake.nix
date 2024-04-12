{
  description = "Flake containing build environment for nigelhaney.com";

  inputs = {
    nixpkgs = {
      url = "nixpkgs/nixos-unstable";
    };
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
  };

  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem(system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
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
