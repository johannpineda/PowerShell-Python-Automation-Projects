import subprocess

def create_user(first, last, dept):
    return subprocess.check_output([
        "powershell",
        "-File", "../powershell/new_user.ps1",
        first, last, dept
    ], text=True)


def reset_password(username):
    return subprocess.check_output([
        "powershell",
        "-File", "../powershell/reset_password.ps1",
        username
    ], text=True)


def run_inventory():
    return subprocess.check_output([
        "powershell",
        "-File", "../powershell/inventory.ps1"
    ], text=True)