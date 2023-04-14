# Import the CSV file
$csvFilePath = "C:\Users\Administrator\Desktop\ous.csv"
$csvData = Import-Csv -Path $csvFilePath

# Loop through each record in the CSV data
foreach ($record in $csvData) {
    # Extract the Name and Path values from the CSV record
    $name = $record.Name
    $path = $record.Path

    # Generate the output string in the desired format
    $output = "{0},{1}" -f $name, $path

    # Print the output string
    Write-Host $output
}
