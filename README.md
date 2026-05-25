

<h1 align="center">🛡️ IT Automation Admin Console</h1>


<p align="center">
  <b>Enterprise-Style IT Operations Dashboard built with PowerShell + Python</b>
</p>

<p align="center">
  <img src="image-2.png" alt="IT Automation Admin Console" width="900"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/PowerShell-Automation-5391FE?style=for-the-badge&logo=powershell" />
  <img src="https://img.shields.io/badge/GUI-Tkinter-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Role--Based-Access-orange?style=for-the-badge" />
</p>


---

## ✨ Overview

The **IT Automation Admin Console** is a role-based desktop administration platform that simulates real-world enterprise IT workflows using:

* ⚡ **PowerShell automation scripts**
* 🖥️ **Python Tkinter GUI dashboard**
* 🏢 Simulated **Active Directory operations**
* 🎫 Internal incident ticket management

This project demonstrates how IT teams can centralize operational tasks into a single administrative interface while automating repetitive system administration workflows.

---

# 🚀 Features

## 👤 User & Account Management

* Automated Active Directory-style user onboarding
* Password reset simulation
* Account unlock functionality
* Role-based permission handling

## 💻 System Administration

* Endpoint/system inventory collection
* Real-time administrative action logging
* PowerShell script execution through Python
* Centralized operations dashboard

## 🎫 Incident Management

* Create and manage incident tickets
* Track support actions
* Simulated internal IT helpdesk workflow

## 🔐 Security & Access Control

* Multi-role login system
* IT / HR / Security role simulation
* Controlled administrative actions

---

# 🧰 Tech Stack

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| **Python**            | GUI application logic           |
| **Tkinter**           | Desktop admin dashboard         |
| **PowerShell**        | IT automation scripting         |
| **JSON**              | Data storage & configuration    |
| **Subprocess Module** | Python ↔ PowerShell integration |

---

# 📸 Dashboard Preview

<p align="center">
  <img src="image-2.png" alt="Dashboard Preview" width="900"/>
</p>

---

# ⚙️ How to Run

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```

## 2️⃣ Navigate to the Python Directory

```bash
cd python
```

## 3️⃣ Launch the Admin Console

```bash
python admin_console.py
```

---

# 🏗️ Project Structure

```bash
IT-Automation-Admin-Console/
│
├── python/
│   ├── admin_console.py
│   └── gui_components/
│
├── powershell/
│   ├── onboarding.ps1
│   ├── password_reset.ps1
│   ├── inventory.ps1
│   └── unlock_account.ps1
│
├── data/
│   ├── users.json
│   └── tickets.json
│
└── README.md
```

---

# 🎯 What This Project Demonstrates

✅ IT automation using PowerShell scripting
✅ Python integration with system-level tools
✅ Enterprise workflow simulation
✅ Role-based administration systems
✅ Desktop GUI application development
✅ Incident management architecture
✅ Administrative logging and operational tooling

---

# 🎥 Project Demo

<p align="center">
  <a href="https://www.youtube.com/watch?v=MJ-y42Vg-Ug">
    <img src="https://img.youtube.com/vi/MJ-y42Vg-Ug/maxresdefault.jpg" width="800" alt="Watch Demo" />
  </a>
</p>

<p align="center">
  ▶️ <b>Click the image above to watch the demo</b>
</p>

---

# 🌟 Future Improvements

* LDAP / real Active Directory integration
* Database-backed ticket storage
* REST API integration
* Multi-machine inventory reporting
* Dark mode UI theme
* Authentication hardening
* Exportable audit logs
