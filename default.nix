 

{pkgs ? import <nixpkgs> {} } :


with pkgs;
let
  my-python-packages = python-packages: with python-packages; [
    
   flask flask-admin  pip  virtualenv gunicorn sqlalchemy flask-bootstrap
    requests  
    # other python packages you want
  ];
  python-with-my-packages = python3.withPackages my-python-packages;
in
# search for this in Emulating virtualenv with nix-shell in nix Wiki

pkgs.mkShell {
  buildInputs = [ python-with-my-packages];
} 
