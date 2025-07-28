# ping_tools

# 🖧 Network Reachability Toolkit

This project contains lightweight Scapy-based Python scripts for basic network testing and automation — designed to run from macOS or Windows on a local subnet.

---

## 📄 Scripts Included

### 1. `ping_mac.py`  
A direct ICMP ping script targeting a MacBook (IP: `192.168.1.248`).

**Purpose**:  
- Quickly verify reachability to a specific host (e.g., your MacBook Pro).
- Useful for connectivity tests and diagnostics.

**Usage**:
```bash
python3 ping_mac.py
```

---

### 2. `ping_sweep_verbose.py`  
A simple ping sweep across the `192.168.1.0/24` subnet.

**Purpose**:
- Scan your local network for live hosts.
- Identify what devices are online.

**Usage**:
```bash
python3 ping_sweep_verbose.py
```

---

## ⚙️ Requirements

Install Scapy first:
```bash
pip3 install scapy
```

---

## ✅ Platform

Tested on:
- macOS (Terminal with Python 3.x)
- Windows 11 (Command Prompt with Python 3.x)

---

## 🧠 Notes

- These scripts use raw sockets. On macOS or Linux, you may need to run with `sudo`:
```bash
sudo python3 ping_mac.py
```

- Default subnet for the sweep is `192.168.1.0/24`. You can edit that in the script.

---

## 👨🏾‍💻 Author

John Felix  
GitHub: [https://github.com/Johnfednyfelix]  
LinkedIn: [https://www.linkedin.com/in/johnfelix/]
