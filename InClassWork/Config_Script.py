import os
import subprocess

## Function that installs the desired packages
def install_packages():
    packages = ["git", "vim", "python3", "snort"]
    for package in packages:
        subprocess.run(["sudo", "apt-get", "install", "-y", package])
 
## Function that installs the desired vim customizations 
def vim_customization():
    
       
## Driver 
if __name__ == "__main__":
    install_packages()
