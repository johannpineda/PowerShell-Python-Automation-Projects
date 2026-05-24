param(
    [string]$Username
)

$newPassword = "Temp@12345!"

Write-Host "Resetting password for $Username"
Write-Host "New password assigned: $newPassword"

Write-Host "Account unlocked (simulated)"