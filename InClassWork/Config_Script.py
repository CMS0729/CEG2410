import os
import subprocess

## Installs the desired packages
def install_packages():
    packages = ["git", "vim", "python3", "snort"]
    for package in packages:
        subprocess.run(["sudo", "apt-get", "install", "-y", package])
       
## Driver 
if __name__ == "__main__":
    install_packages()