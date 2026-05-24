param(
    [string]$FirstName,
    [string]$LastName,
    [string]$Department
)

$username = ($FirstName.Substring(0,1) + $LastName).ToLower()

Write-Host "Creating user: $username"
Write-Host "Department: $Department"

# SIMULATED AD ACTION (safe for non-domain machines)
Write-Host "User created successfully in Active Directory (simulated)"