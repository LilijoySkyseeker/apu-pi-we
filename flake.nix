{
  description = "Apupiwe: tools for the language";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};

      # The Resource Grammar Library (compiled release): GF's English and other language grammars.
      gf-rgl = pkgs.stdenvNoCC.mkDerivation {
        pname = "gf-rgl";
        version = "20260403";
        src = pkgs.fetchurl {
          url = "https://github.com/GrammaticalFramework/gf-rgl/releases/download/20260403/gf-rgl-20260403.zip";
          sha256 = "1sqf4l320iamgmyyfb00rp4l0c506v052zv46hxzgbg3b5745ad1";
        };
        nativeBuildInputs = [ pkgs.unzip ];
        installPhase = "mkdir -p $out && cp -r ./* $out/";
      };

      # Grammatical Framework 3.12. The nixpkgs package is broken (its Setup.hs doesn't build with
      # current Cabal), so this uses the official Ubuntu binary with its library paths patched.
      gf = pkgs.stdenv.mkDerivation {
        pname = "gf";
        version = "3.12";
        src = pkgs.fetchurl {
          url = "https://github.com/GrammaticalFramework/gf-core/releases/download/release-3.12/gf-3.12-ubuntu-24.04.deb";
          sha256 = "1n5l6qjsf340qgigvvlnzfzsq9m9k3cvm8am0w5f1w8knx959ahp";
        };
        nativeBuildInputs = [ pkgs.dpkg pkgs.autoPatchelfHook pkgs.makeWrapper ];
        buildInputs = [ pkgs.gmp pkgs.ncurses ];
        unpackPhase = "dpkg-deb -x $src .";
        installPhase = ''
          mkdir -p $out/bin $out/lib $out/share
          cp usr/bin/gf $out/bin/
          cp -P usr/lib/libpgf.so* usr/lib/libgu.so* $out/lib/
          cp -r usr/share/x86_64-linux-ghc-*/gf-* $out/share/ || true
          wrapProgram $out/bin/gf --set-default GF_LIB_PATH ${gf-rgl}
        '';
      };
    in {
      packages.${system} = { inherit gf gf-rgl; };

      devShells.${system}.default = pkgs.mkShell {
        packages = [
          (pkgs.python3.withPackages (ps: [
            ps.numpy     # words.py, build.py
            ps.wordfreq  # offensive.py
            ps.lark      # parse.py
            ps.markdown  # site.py
          ]))
          gf             # the formal grammar (grammar/)
        ];
      };
    };
}
