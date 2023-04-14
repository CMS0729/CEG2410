Import-Csv ous.csv | foreach {
    $name = $_.Name
    $path = $_.Path
    $ou = New-ADOrganizationalUnit -Name $name -Path $path `
    -ProtectedFromAccidentalDeletion $true -PassThru
    Write-Host "Organizational Unit '$name' with Path '$path' has been created."
}
