# Project 2 - DIY NAS

### Name: Cody Southworth

## Part 1 - NFS Server Configuration

1. Configure a space, use the `ext4` filesystem
    - Commands used:
        - "sudo sgdisk -n 1:0:0 /dev/xvdf" and "sudo sgdisk -n 1:0:0 /dev/xvdg"
            - The purpose of this command is to partition the disks. 
        - sudo mdadm --create --verbose /dev/md0 --level=0 --raid-devices=2 /dev/xvd[f-g]1
            - The purpose of this command is to create a RAID0 array. 
        - sudo mdadm --detail /dev/md0
            - The purpose of this command is to bring up a prompt that esnures the array is working. If it is we should see "State: clean". 
        - sudo mdadm --detail --scan --verbose | sudo tee -a /etc/mdadm/mdadm.conf
            - This is to esnure the array will persist after reboot. 
        - sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0 /dev/md0
            - This command will format the array.
2. `mount` the partition to a folder on your AWS instance.  Allow `other`s to add files / folder and edit files / folders within the folder.
    - Commands used:
        - sudo mkdir /mnt/NFS\ Server
        - sudo mount /dev/md0 /mnt/NFS\ Server
        - df -h
        - sudo blkid
        - sudo chmod o+rw /mnt/NFS\ Server
3. Configure `/etc/fstab` to auto mount the partition to the folder on boot.
    - Line added to `/etc/fstab`:
        - UUID="d686850e-b453-42de-afed-0f8e4ce0cef2 /mnt/NFS\ Server ext4 defaults 0 0
    - Command to test `/etc/fstab`:
        - mount -a
4. Install `nfs` server 
    - Command to install:
        - sudo apt install nfs-kernel-server
    - Command to check service status:
        - service nfs-kernel-server status
5. Configure `/etc/exports` to share folder
    - Line added to `/etc/exports`:
        - "/mnt/NFS Server" 52.5.187.202(rw,sync,no_subtree_check)
    - Reasoning for options:
        - "rw"
            - I choose this option because it allows both read and write requests on this NFS volume. The default is to disallow any request which changes the filesystem.
        - "sync"
            - This option means that all changes to the according filesystem are immediately flushed to disk.
        - "no_subtree_checking"
            - This option disables subtree checking, which has mild security implications, but can improve reliability.
6. Enable your `nfs` share
    - Command to export all directories in `/etc/exports`:
        - exportfs -a 
    - Command to restart `nfs`:
        - sudo systemctl restart nfs-kernel-server
7. Screenshots:
    - ![My Image](Screenshots/BlockDevices.png)
    - ![My Image](Screenshots/PermissionsShareableFolder.png)
    - ![My Image](Screenshots/FoldersShared.png)

## Part 2 - Firewall Fixes

1. Screenshot:
    - ![My Image](Screenshots/InboundRules.png)

## Part 3 - Mounting an NFS Share

1. How to unmount a nfs share:
    - This is rather simple. All we need to do is figure out which nfs we would like to unmount and use the command "sudo umount /nfs/your_folder_name". 

2. Screenshots:
    - ![My Image](Screenshots/ClientNFS.png)
    - ![My Image](Screenshots/NFSMount.png)
