import os
import subprocess

def install_packages():
    packages = ["git", "vim", "python3", "snort"]
    for package in packages:
        subprocess.run(["sudo", "apt-get", "install", "-y", package])
        
if __name__ == "__main__":
    install_packages()
