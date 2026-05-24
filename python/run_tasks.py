import subprocess

def run_user():
    subprocess.run([
        "powershell",
        "-File",
        "../powershell/new_user.ps1",
        "John",
        "Smith",
        "IT"
    ])

def run_reset():
    subprocess.run([
        "powershell",
        "-File",
        "../powershell/reset_password.ps1",
        "jsmith"
    ])

def run_inventory():
    subprocess.run([
        "powershell",
        "-File",
        "../powershell/inventory.ps1"
    ])

run_user()
run_reset()
run_inventory()