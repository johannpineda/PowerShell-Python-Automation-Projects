import tkinter as tk
from tkinter import ttk, messagebox

from auth import authenticate
from ad_bridge import create_user, reset_password, run_inventory
from tickets import create_ticket, get_tickets

# ---------------- APP ----------------
app = tk.Tk()
app.title("IT Admin Console")
app.geometry("1100x700")

current_user = None

# ---------------- LOGIN ----------------
login_frame = tk.Frame(app)
login_frame.pack(fill="both", expand=True)

tk.Label(login_frame, text="Login", font=("Arial", 18)).pack(pady=10)

user_entry = tk.Entry(login_frame)
user_entry.pack()

pass_entry = tk.Entry(login_frame, show="*")
pass_entry.pack()


def login():
    global current_user
    user = authenticate(user_entry.get(), pass_entry.get())

    if user:
        current_user = user
        login_frame.pack_forget()
        dashboard_frame.pack(fill="both", expand=True)
        log(f"Logged in as {user['role']}")
    else:
        messagebox.showerror("Login failed", "Invalid credentials")


tk.Button(login_frame, text="Login", command=login).pack(pady=10)

# ---------------- DASHBOARD ----------------
dashboard_frame = tk.Frame(app)

# ---- LOG BOX ----
log_box = tk.Text(dashboard_frame, height=10)
log_box.pack(fill="x")

def log(msg):
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)

# ---------------- AD ACTIONS ----------------

def onboard():
    res = create_user("John", "Smith", "IT")
    log(res)

def reset():
    res = reset_password("jsmith")
    log(res)

def inventory():
    res = run_inventory()
    log(res)

# ---------------- BUTTONS ----------------
btn_frame = tk.Frame(dashboard_frame)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Create User", command=onboard).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Reset Password", command=reset).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Run Inventory", command=inventory).grid(row=0, column=2, padx=5)

# ---------------- TICKETS ----------------
ticket_frame = tk.Frame(dashboard_frame)
ticket_frame.pack(pady=20)

tk.Label(ticket_frame, text="Create Ticket").grid(row=0, column=0)

title_entry = tk.Entry(ticket_frame)
title_entry.grid(row=0, column=1)

priority_box = ttk.Combobox(ticket_frame, values=["Low", "Medium", "High"])
priority_box.grid(row=0, column=2)
priority_box.set("Low")


def add_ticket():
    ticket = create_ticket(title_entry.get(), user_entry.get(), priority_box.get())
    log(f"Ticket created: {ticket}")


tk.Button(ticket_frame, text="Submit Ticket", command=add_ticket).grid(row=0, column=3)

# ---------------- TICKET LIST ----------------
list_box = tk.Listbox(dashboard_frame, width=80)
list_box.pack()

def refresh_tickets():
    list_box.delete(0, tk.END)
    for t in get_tickets():
        list_box.insert(tk.END, f"#{t['id']} {t['title']} [{t['priority']}] - {t['status']}")

tk.Button(dashboard_frame, text="Refresh Tickets", command=refresh_tickets).pack()

# ---------------- START ----------------
app.mainloop()