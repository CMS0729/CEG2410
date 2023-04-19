import os
import subprocess

# Function that installs the desired packages
def install_packages():
    ## Variable packages that stores each package in a list.
    packages = ["git", "vim", "python3", "snort"]
    ## For loop to install each individual package.
    for package in packages:
        subprocess.run(["sudo", "apt-get", "install", "-y", package])
 
# Function that installs the desired vim customizations 
def vim_customization():
    # Change default colorization
    with open(os.path.expanduser("~/.vimrc"), "a") as f:
        f.write("syntax on\n")
        
    # Add functionality
      with open(os.path.expanduser("~/.vimrc"), "a") as f:
       # Link to where I got idea: https://linuxhandbook.com/vim-indentation-tab-spaces/
         f.write("set noexpandtab\n")
         f.write("set tabstop=4\n")
         f.write("set shiftwidth=4\n")
        
    # Change color scheme
      with open(os.path.expanduser("~/.vimrc"), "a") as f:
      # Changes the color scheme to `desert`.
      f.write("colorscheme desert\n")
        
## Function to copy the `authorized_keys` to `.ssh`
def copy_authorized_keys():
    # Creates `ssh_dir` variable which points to the directory `~/.ssh`.
    ssh_dir = os.path.expanduser("~/.ssh")
    # Creates the directory.
    os.makedirs(ssh_dir, exist_ok=True)
    # Copys the authorized_keys file to the pointed directory
    subprocess.run(["cp", "authorized_keys", ssh_dir])
       
# Driver 
if __name__ == "__main__":
    # Calls the install_packages function
    install_packages()
    # Calls the vim_customization function
    vim_customization()
    # Calls the copy_authorized_keys function
    copy_authorized_keys()
