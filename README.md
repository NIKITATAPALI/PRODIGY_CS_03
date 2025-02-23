# 🔐 Password Strength Assessment Tool

This project provides a **password strength assessment tool** using **Python, Bash, and Python Dash (Web App)**. It helps users evaluate password strength based on:

🌚 **Length of the password**  
🌚 **Presence of uppercase and lowercase letters**  
🌚 **Inclusion of numbers**  
🌚 **Usage of special characters**  
🌚 **Feedback for improvement**

---

## 🚀 Features
- **Displays a custom ASCII banner** at the start of the script.
- **Evaluate password strength** using predefined security rules.
- **Provide user-friendly feedback** on password improvements.
- **Works as a Command Line Interface (CLI) using Python & Bash.**
- **Includes a Graphical User Interface (GUI) Web App using Dash.**
- **Compatible with Linux, Windows, and macOS.**

---

## 📌 Installation & Usage Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/NIKITATAPALI/PRODIGY_CS_03.git
```
Or manually create the script files:
```bash
nano password_checker.py  # For Python
nano password_checker.sh   # For Bash
nano password_strength_dash.py                # For Dash Web App
```
Copy and paste the respective script into the file and save.

---

## 🔹 Python Implementation (CLI)

### 📞 ASCII Banner
When running the Python script, the following banner will be displayed:
```
██████╗  █████╗ ███████╗███████╗███████╗███████╗████████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝╚══██╔══╝
██████╔╝███████║███████╗███████╗███████╗█████╗     ██║   
██╔═══╝ ██╔══██║╚════██║╚════██║╚════██║██╔══╝     ██║   
██║     ██║  ██║███████║███████║███████║███████╗   ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝   
Version: 1.0
Tool Created by Nikita Tapali
Contact: kynic406@gmail.com
```

### 📞 Install Dependencies
```bash
pip install colorama
```

### ▶️ Run the Python Script
```bash
python3 password_strength.py
```

### 📝 Example Usage:
```bash
Enter a password: P@ssw0rd123

🌚 Your password is very strong!
```

---

## 🔹 Bash Implementation (CLI)

### 📞 ASCII Banner
When running the Bash script, the following banner will be displayed:
```
██████╗  █████╗ ███████╗███████╗███████╗███████╗████████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝╚══██╔══╝
██████╔╝███████║███████╗███████╗███████╗█████╗     ██║   
██╔═══╝ ██╔══██║╚════██║╚════██║╚════██║██╔══╝     ██║   
██║     ██║  ██║███████║███████║███████║███████╗   ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝   
Version: 1.0
Tool Created by Nikita Tapali
Contact: kynic406@gmail.com
```

### 📞 Make the Script Executable
```bash
chmod +x password_checker.sh
```

### ▶️ Run the Bash Script
```bash
./password_checker.sh
```

### 📝 Example Usage:
```bash
Enter a password: test123

❌ Weak password. Please improve it.
❌ Password should contain at least one uppercase letter.
❌ Password should contain at least one special character.
```

---

## 🔹 Python Dash Web App (GUI)

### 📞 Install Dependencies
```bash
pip install dash dash-bootstrap-components
```

### ▶️ Run the Web App
```bash
python3 password_strength_dash.py
```

### 🌐 Access the App in Your Browser
```
http://127.0.0.1:8050/
```

### 📝 Example UI Output:
```
Password: Secure@123
✅ Strong Password!
```

---

## 🔧 Dependencies
### Python Version:
- `colorama`
- `dash` (for web app)
- `dash-bootstrap-components`

### Bash Version:
- Works on any standard Linux shell.

---

## 🛠 Tested On:
- **Ubuntu**
- **Debian**
- **Kali Linux**
- **Windows (Python version only)**

---

## 🐜 License
This project is licensed under the MIT License.

---

## 🤝 Contributing
Want to contribute? Fork the repo and submit a pull request.

---

## 📢 Find Me On:
<p align="left">
  <a href="https://github.com/NIKITATAPALI/" target="_blank"><img src="https://img.shields.io/badge/Github-blue?style=for-the-badge&logo=github"></a>
</p>

---

## ⚠️ Disclaimer

<i>This project is created for educational purposes only. Ensure compliance with applicable security laws before using this tool.</i>

---

### 🎉 Thanks to all contributors!
