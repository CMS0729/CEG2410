# Read default password as secure string from user input
$secpass = Read-Host "Enter Default Password for Accounts" -AsSecureString

# Import CSV file
$csvPath = "C:\Users\Administrator\Desktop\users.csv"
$users = Import-Csv $csvPath

# Loop through each user in the CSV and create user accounts
foreach ($user in $users) {
    # Create user account with New-ADUser cmdlet
    New-ADUser -Name "$($user.FirstName) $($user.LastName)" `
        -SamAccountName $user.SamAccountName `
        -Path "OU=$($user.OU2),OU=$($user.OU1),DC=example,DC=com" `
        -Enabled $true `
        -AccountPassword $secpass
}
