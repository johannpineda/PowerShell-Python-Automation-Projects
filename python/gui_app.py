import tkinter as tk
import subprocess

# ---------- FUNCTIONS ----------

def run_onboard():
    result = subprocess.check_output([
        "powershell",
        "-File",
        "../powershell/new_user.ps1",
        "John",
        "Smith",
        "IT"
    ], text=True)
    output_box.insert(tk.END, "\n[ONBOARD]\n" + result)

def run_reset():
    result = subprocess.check_output([
        "powershell",
        "-File",
        "../powershell/reset_password.ps1",
        "jsmith"
    ], text=True)
    output_box.insert(tk.END, "\n[RESET]\n" + result)

def run_inventory():
    result = subprocess.check_output([
        "powershell",
        "-File",
        "../powershell/inventory.ps1"
    ], text=True)
    output_box.insert(tk.END, "\n[INVENTORY]\n" + result)

# ---------- UI SETUP ----------

app = tk.Tk()
app.title("IT Automation Console")
app.geometry("700x500")

# Buttons
tk.Button(app, text="Create User", command=run_onboard).pack(pady=5)
tk.Button(app, text="Reset Password", command=run_reset).pack(pady=5)
tk.Button(app, text="Run Inventory", command=run_inventory).pack(pady=5)

# Output box
output_box = tk.Text(app, height=25, width=80)
output_box.pack(pady=10)

# Run app
app.mainloop()