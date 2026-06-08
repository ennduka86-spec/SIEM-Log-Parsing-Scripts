# SIEM-Log-Parsing-Scripts
Scripts for parsing and normalizing SIEM logs (Splunk, Microsoft Sentinel) to automate alert triage and improve SOC efficiency.
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Security Scan](https://img.shields.io/badge/security-scanned-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Python](https://img.shields.io/badge/python-3.10-blue)
![PowerShell](https://img.shields.io/badge/powershell-5.1-lightblue)
![Bash](https://img.shields.io/badge/bash-4.4-black)

🏗️ Box‑Style Architecture Diagram
```markdown
┌───────────────────────────────┐
│       SIEM Log Parser         │
│   (Python, JSON → CSV)        │
└───────────────┬───────────────┘
                │
┌───────────────┴───────────────┐
│   Event Parser (PowerShell)   │
│   (Windows Event Logs → CSV)  │
└───────────────┬───────────────┘
                │
┌───────────────┴───────────────┐
│   SSH Filter (Bash Script)    │
│   (Auth Logs → Failed Logins) │
└───────────────┬───────────────┘
                │
┌───────────────┴───────────────┐
│ MITRE ATT&CK Mapper (Python)  │
│   (Logs → ATT&CK Techniques)  │
└───────────────┬───────────────┘
                │
┌───────────────┴───────────────┐
│   Output Datasets Folder       │
│   (sample.log, mapped_logs.csv)│
└───────────────────────────────┘
```




## 📊 Workflow Diagram (Mermaid)

### Incident Response Lifecycle
```mermaid
flowchart TD
    Alert --> Triage --> Escalation --> Containment --> Eradication --> Recovery --> Lessons
