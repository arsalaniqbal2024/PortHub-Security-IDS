# 🛡️ PortHub Security IDS

> **Real-Time Network Intrusion Detection System (NIDS) built with Python, Scapy, Flask, and SQLite**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Dashboard-black?logo=flask)
![Scapy](https://img.shields.io/badge/Scapy-Packet%20Analysis-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Overview

PortHub Security IDS is a lightweight **Network Intrusion Detection System (NIDS)** developed in Python that monitors live network traffic and detects common network attacks in real time.

The system captures packets using **Scapy**, analyzes them through modular detection engines, stores alerts in an **SQLite database**, and displays security events through a modern **Flask-based SOC dashboard**.

The project was built as part of my cybersecurity portfolio to demonstrate practical knowledge of:

- Network Security
- Intrusion Detection Systems
- Python Development
- SOC Monitoring
- Security Analytics

---

# ✨ Features

- ✅ Real-time Packet Capture
- ✅ Port Scan Detection
- ✅ SSH Connection Monitoring
- ✅ FTP Connection Monitoring
- ✅ ICMP Flood Detection
- ✅ Telnet Access Detection
- ✅ Risk Score Calculation
- ✅ Alert Logging
- ✅ SQLite Database Integration
- ✅ Interactive Dashboard
- ✅ Charts & Analytics
- ✅ Responsive SOC-style Interface

---

# 🏗 Architecture

```

Network Traffic
│
▼
Scapy Packet Capture
│
▼
Packet Handler
│
├──────────────┬──────────────┬──────────────┬──────────────┐
│              │              │              │              │
▼              ▼              ▼              ▼              ▼
Port Scan      SSH           FTP          ICMP          Telnet
Detector      Monitor       Monitor      Detector      Monitor
│
▼
Alert Manager
│
├──────────────┐
│              │
▼              ▼
alerts.log     SQLite Database
│
▼
Flask Dashboard
│
▼
Security Analytics
