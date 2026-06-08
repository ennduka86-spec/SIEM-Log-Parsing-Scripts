# SIEM-Log-Parsing-Scripts
Scripts for parsing and normalizing SIEM logs (Splunk, Microsoft Sentinel) to automate alert triage and improve SOC efficiency.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Security Scan](https://img.shields.io/badge/security-scanned-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Python](https://img.shields.io/badge/python-3.10-blue)
![PowerShell](https://img.shields.io/badge/powershell-5.1-lightblue)
![Bash](https://img.shields.io/badge/bash-4.4-black)

# 🚀 Quickstart
```bash
git clone https://github.com/yourusername/SIEM-Log-Parsing-Scripts.git
cd SIEM-Log-Parsing-Scripts
python scripts/log_parser.py datasets/sample.log parsed_logs.csv

# ✨ Features
- Add Splunk detection queries
- Automate AWS GuardDuty parsing
- Build compliance dashboards

# 📊 Workflow
- Alert → SIEM generates an alert from raw logs.
- Triage → Your scripts normalize logs, making them easier to analyze.
- Escalation → Enriched logs (with MITRE ATT&CK mapping) help analysts decide if escalation is needed.
- Containment → Parsed data supports quick response actions.
- Eradication → Analysts use structured logs to remove threats.
- Recovery → Clean logs help validate system recovery.
- Lessons → Output datasets feed back into detection engineering.

# 🔮 Future Work
- Splunk Detection Queries → Add SPL queries for automated detection.
- AWS GuardDuty Automation → Scripts to parse GuardDuty findings.
- Compliance Dashboards → Build dashboards for PCI‑DSS, HIPAA, SOC2.
- Elastic Security Integration → Extend parsing to Elastic SIEM.
- Threat Hunting Playbooks → Add MITRE ATT&CK‑aligned hunting guides.
- XDR Expansion → Integrate with Microsoft Defender XDR or Palo Alto Cortex.

## 🔎 Input vs Output Demo

**Input (`sample.log`):**
```json
{"timestamp": "2026-06-09T02:00:00Z", "event_id": 4624, "user": "ejike", "action": "LogonSuccess", "source_ip": "192.168.1.10"}
{"timestamp": "2026-06-09T02:05:00Z", "event_id": 4625, "user": "unknown", "action": "LogonFailure", "source_ip": "203.0.113.45"}



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
