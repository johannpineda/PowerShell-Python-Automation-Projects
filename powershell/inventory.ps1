# Ensure output folder exists
$outputDir = ".\output"

if (!(Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

$computers = @(
    "PC-01",
    "PC-02",
    "PC-03"
)

$result = foreach ($pc in $computers) {
    [PSCustomObject]@{
        ComputerName = $pc
        Status = "Online"
        OS = "Windows 11 (Simulated)"
    }
}

$result | Format-Table -AutoSize

$result | ConvertTo-Json | Out-File "$outputDir\inventory.json"