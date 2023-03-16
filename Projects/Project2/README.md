# Project 2 - DIY NAS

### Name: Cody Southworth

## Part 1 - NFS Server Configuration

1. Configure a space, use the `ext4` filesystem
    - Commands used:
        - "sudo sgdisk -n 1:0:0 /dev/xvdf" and "sudo sgdisk -n 1:0:0 /dev/sda"
        - sudo mdadm --create --verbose /dev/md0 --level=0 --raid-devices=2 /dev/xvd[f-g]1
        - sudo mdadm --detail /dev/md0
        - sudo mdadm --detail --scan --verbose | sudo tee -a /etc/mdadm/mdadm.conf
        - sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0 /dev/md0
        - 
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
3. Install `nfs` server 
    - Command to install:
        - sudo apt install nfs-kernel-server
    - Command to check service status:
        - service nfs-kernel-server status
4. Configure `/etc/exports` to share folder
    - Line added to `/etc/exports`:
        - "/mnt/NFS Server" 44.214.94.251(rw,sync,no_subtree_check)
    - Describe the options you used in exports and why.  If you used no options, describe all default options that would apply.
5. Enable your `nfs` share
    - Command to export all directories in `/etc/exports`:
        - exportfs -a 
    - Command to restart `nfs`:
        - sudo systemctl restart nfs-kernel-server

Screenshot your block devices (`lsblk`), the permissions of your shareable folder, and what folders are currently shared (`exportfs`)

## Part 2 - Firewall Fixes

Go to the Learner Lab page, make sure "Start Lab" turned things on, then click the AWS link.  Now go to EC2 -> Security Groups.  You'll see one labeled something like: `ceg2350-Lab1SecurityGroup`

If you set `ufw` rules or `iptables` on your instance, I recommend disabling them (`ufw`) or flushing them (`iptables`).  If you would rather keep using them, I'm good with that.

Outbound rules: 
- leave outbound rules as default ALLOW
- some of you messed with them in project 1.  This is a reminder to undo that ;)

Inbound rules:
- ALLOW `https` from any IPv4 address (can add IPv6)
- ALLOW `http` from any IPv4 address (can add IPv6)
- ALLOW `ssh` from "home" - public IP from ISP
- ALLOW `ssh` from WSU - 130.108.0.0/16
- ALLOW `ssh` within virtual network - 10.0.0.0/16
- ALLOW `nfs` from "home" - public IP from ISP
- ALLOW `nfs` from WSU - 130.108.0.0/16
- ALLOW `nfs` within virtual network - 10.0.0.0/16

Screenshot your updated Inbound rules and include it with your documentation

## Part 3 - Mounting an NFS Share

Linux and Mac can mount using NFS.  WSL2 can work, but is being a butt about it.  To make less of a headache, we will use our same AWS instance as a client.

For this portion, mount your share folder to the client.

1. Install NFS client
2. Create a directory to mount the NFS share to
3. Mount the share folder using the host's IP (public or private)
4. Prove that you can add files to the `nfs` share
5. Document how to `unmount` the `nfs` share

Screenshot what is currently mounted by `nfs` clients using `nfsstat` and include it with your documentation.

## Recommended Resources

- [Ubuntu Server Docs - NFS](https://ubuntu.com/server/docs/service-nfs)
- [Digital Ocean - Set up an NFS mount](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-20-04)
- [RedHat - `/etc/exports` & `exportfs`](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/deployment_guide/s1-nfs-server-config-exports) 
- [Geek Diary - Understanding the `/etc/exports` file](https://www.thegeekdiary.com/understanding-the-etc-exports-file/)

## Extra Credit - WSL2 or Mac as a client (15%)

Why is this extra credit?  WSL2 + Ubuntu can work as an NFS client, but it involves a bit of magic to kick it along.  For extra credit, create a guide for mounting an NFS share to WSL2.  I will award credit if you don't crack it, but do show and document what you tried.  I will award credit if it just works, and again, you document what steps you needed (and maybe provide your version numbers of things for WSL2 and Windows)

`rpc` is what is causing most headaches, and it is mostly acting up because WSL2 is magic and doesn't have true `systemd`

- [SuperUser - rpc-statd is not running](https://superuser.com/questions/657071/mount-nfs-rpc-statd-is-not-running-but-is-required-for-remote-locking)
- [SuperUser - how to mount NFS in WSL2?](https://superuser.com/questions/1667722/how-to-mount-an-nfs-share-on-wsl2)
