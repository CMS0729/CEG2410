# Project 3

### Name: Cody Southworth

## Setup AD DC

- Configuring a Windows Server to be a Domain Controller
  - EC2:
    - Firstly you need to launch a new Instance. You can give it a name whatever you prefer in my case I named it ```Windows Server 2019```. Next give it an Image and I choose "Windows 2019 Base". Setup your Network Settings to your active running linux instance. Next you need to setup your security group.
    - Once that is all done we now need to give our new instance an elastic IP. Create one and name it however you choose but make sure to assoicate it with your Linux instance. Last thing we need to do is change our inbound settings. Make sure to allow RSD from your home IP and your aws instance IP. 
   - In the System:
      - Our next step is to install Active Directory Domain Services or AD DS for short. To do this we need to open the Windows Powershell and in the terminal put ```Install-WindowsFeature -name AD-Domain-Services -IncludeManagementTools```. This will give you the tools to get the ball rolling.
  - Network Settings:
      - We now need to edit our network settings. Open powershell and enter ```ipconfig /all```. Once you are in the control panel edit your IPv4 settings and take a look at your powershell so you correctly inputting everyting. Change your public IP to the given one in the powershell, change your subnet mask to ```255.255.0.0```. Then change the DNS server to the one listed in powershell. Your machine will need to restart.
  - Computer Name:
    - Next we need to change the PC name. Once again back to the control panel. It is of good habit to name your first domain controller to "DC1". You will need to restart once again to apply the changes.
  - Server Manager:
    - Once in the Server Manager we need to promote this server to a domain controller. Once that is done you will be prompted with a menu to setup the deployment configuration. You will want to add a new forest and give it a root domain name of your choosing. After that just follow through the wizard until it is installed. Your system will need to restart once again. 
- Domain Name: ```ad.taiga.com```
- Domain Controller Name: ```DC1```
- Domain DNS IP: ```10.0.0.2```

## AD Structure

### Create OUs

Create the following Organizational Units - Provide screenshot proof:

- `[Domain] Computers` - client / user machines
  - `Conference` - publicly accessible kiosks and presentation devices
  - `Secure` - machines for HR and finance users
  - `Workstations` - machines for devs and engineers
- `[Domain] Servers` - servers for org (data shares, repo hosts, HPCs)
- `[Domain] Users`
  - `Finance` - can log on to Secure computers, managed by hr_finance_admins group
  - `HR` - can log on to Secure computers, managed by hr_finance_admins group
  - `Engineers` - can log on to Workstations, managed by dev_eng_admins
  - `Developers` - can log on to Workstations, managed by dev_eng_admins
- Screenshot: *CBC*: ![My Image](Screenshot/users.png)

**Extra Credit (5%)** Provide a scripted solution that generates these. There may be a sample `.csv` file in this folder

### Joining Users

Using a PowerShell script, join the users in [users.csv](users.csv) to your domain. Make sure `domain User` is corrected to your `OU` name. The users need to be organized into the [Domain] Users OU and into their corresponding child OUs.

- Add csv file of users and PowerShell script to your repo.
- Screenshot that users are in correct OUs
  - one screenshot is sufficient, just need to see concept is accomplished

**Extra Credit (5%)** Provide a scripted solution to add users to the OUs given in the OU1 and OU2 column.

### Joining Computers

Create another Windows Server instance in AWS on your VPC. Write the steps needed to join the Windows Server to the Domain in the `[Domain] Computers` OU. Provide screenshot proof of success.

- Resources:
  - https://adamtheautomator.com/add-computer-to-domain/
  - Don't forget that DNS step ;)

### Creating Groups

Create the following Security Groups and define where they should be within the OUs based on their roles:

- `project_repos_RW` - users who have Read / Write access to project repositories
    - ```Placed within "taiga Users" (OU1), "Admins" (OU2)```
- `finance_RW` - users who have Read / Write access to finance share
    - ```Placed within "taiga Users" (OU1), "Finance" (OU2)```
- `onboarding_R` - users who have Read access to onboarding documents
    - ```Placed within "taiga Users" (OU1), "Admins" (OU2)```
- `server_access` - users who can log on to Servers
    - ```Placed within "taiga Servers" (OU1)```
- `dev_eng_admins` - IT admins to handle Developer and Engineer accounts
    - ```Placed within "taiga Users" (OU1), "Admins" (OU2)```
- `hr_finance_admins` - IT admins to handle HR and finance accounts
    - ```Placed within "taiga Users" (OU1), "Admins" (OU2)```
- `remote_workstation` - Group of workstations that allow RDP connections
    - ```Placed within "taiga Computers" (OU1), "Workstations" (OU2)```

---

## OUs & GPOs

### Applying Group Policies

Find guides to create the following Group Policy Objects and specify where they should be applied.

- Lock out Workstations after 15 minutes of inactivity.
- Prevent execution of programs on computers in Secure OU
- Disable Guest account login to computers in Secure OU
- Allow server_access to sign on to Servers
- Set Desktop background for Conference computers to company logo.
- Allow users in `remote_workstation` group to RDP to Workstations

**Extra Credit (5%)** Create and apply one of these policies, and show proof it worked.

- The Windows Server you joined to the domain can serve as a good dummy here

### Managing OUs

More people are joining the IT/ administration side of things. Note: you can promote from within or create some new users

Join at least one person to the `hr_finance_admins` and `eng_dev_admins` groups, respectively. Delegate control of the OUs corresponding to the appropriate admin groups.

Document how to delegate control of an OU to a group, which OUs they now delegate, and what permissions they were given (and why you think the scope is appropriate)

- Resources
- https://theitbros.com/active-directory-organizational-unit-ou/

## Submission

In the Pilot Dropbox, paste the URL to your submission
  - URL should look like: https://github.com/WSU-kduncan/ceg2410-YOURGITHUBUSERNAME/blob/main/Windows

Contents should include:
- `README.md`
- csv file(s) (for EC)
- PowerShell script(s) (for EC)
