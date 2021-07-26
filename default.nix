 

{pkgs ? import <nixpkgs> {} } :


with pkgs;
let
  my-python-packages = python-packages: with python-packages; [
  
	 pip flask flask-admin sqlalchemy flask_sqlalchemy flask_wtf email_validator
        flask-bcrypt flask_login 
  
 requests  
    # other python packages you want
  ];
  python-with-my-packages = python3.withPackages my-python-packages;
in
# search for this in Emulating virtualenv with nix-shell in nix Wiki

pkgs.mkShell {
  buildInputs = [ python-with-my-packages];
} 

