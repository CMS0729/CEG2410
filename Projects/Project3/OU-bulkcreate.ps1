$secpass = Read-Host "Enter Default Password for Accounts" -AsSecureString

Import-Csv C:\Users\Administrator\Desktop\users.csv |
foreach {
    $ou1 = $_.OU1
    $ou2 = $_.OU2
    $ouPath = "OU=$ou2,OU=$ou1,DC=ad,DC=taiga,DC=com"
    $userProps = @{
        Name = $_.FirstName + "," + $_.LastName
        GivenName = $_.FirstName
        Surname = $_.LastName
        SamAccountName = $_.SamAccountName
        UserPrincipalName = "$($_.SamAccountName)@adtaiaga.com"
        AccountPassword = $secpass
        Path = $ouPath
        Enabled = $true
    }
    New-ADUser @userProps
}
