### SIEM-Log-Parsing-Scripts
Scripts for parsing and normalizing SIEM logs (Splunk, Microsoft Sentinel) to automate alert triage and improve SOC efficiency.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Security Scan](https://img.shields.io/badge/security-scanned-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Python](https://img.shields.io/badge/python-3.10-blue)
![PowerShell](https://img.shields.io/badge/powershell-5.1-lightblue)
![Bash](https://img.shields.io/badge/bash-4.4-black)

This repository demonstrates SOC automation skills by parsing SIEM logs across Python, PowerShell, and Bash, enriching them with MITRE ATT&CK techniques, and documenting workflows for incident response.

### 🚀 Quickstart
```bash
git clone https://github.com/yourusername/SIEM-Log-Parsing-Scripts.git
cd SIEM-Log-Parsing-Scripts
python scripts/log_parser.py datasets/sample.log parsed_logs.csv

### 🛠 Usage Examples
```bash
python scripts/log_parser.py datasets/sample.log parsed_logs.csv
./scripts/ssh_filter.sh datasets/auth.log
.\scripts\event_parser.ps1
  
```
### 📂 Repository Structure
```text
SIEM-Log-Parsing-Scripts/
│
├── scripts/                         # Core automation scripts
│   ├── log_parser.py                # Python: JSON → CSV parsing
│   ├── event_parser.ps1             # PowerShell: Windows Event Logs → CSV
│   ├── ssh_filter.sh                # Bash: filter failed SSH logins
│   └── mitre_mapper.py              # Python: map logs to MITRE ATT&CK techniques
│
├── datasets/                        # Input and output log samples
│   ├── sample.log                   # Raw input logs (JSON format)
│   └── mapped_logs.csv              # Enriched output logs (CSV with MITRE mapping)
│
├── docs/                            # SOC documentation & playbooks
│   ├── incident_response_template.md
│   ├── ssh_failed_login_playbook.md
│   ├── suspicious_logon_playbook.md
│   ├── malware_infection_playbook.md
│   └── phishing_email_playbook.md
│
├── tests/                           # (Future) Unit tests for scripts
│   └── test_log_parser.py
│
├── configs/                         # (Future) Config files for SIEM integrations
│   └── splunk_queries.conf
│
├── README.md                        # Project overview and usage guide
├── LICENSE                          # MIT License
└── .gitignore                       # Ignore unnecessary files

```

### ✨ Features
- Add Splunk detection queries
- Automate AWS GuardDuty parsing
- Build compliance dashboards


### 📊 Workflow
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

#📈 Future Enhancements
- Dockerized deployment → Package scripts into containers for portability.
- Elastic Security integration → Extend parsing to Elastic SIEM workflows.
- Markdown SOC playbooks → Document incident response procedures in Markdown for easy sharing.
- Cloud SIEM integration → Extend parsing to AWS Security Hub or Azure Sentinel APIs for enterprise‑scale monitoring.
 
## 🔎 Input vs Output Demo

**Input (`sample.log`):**
```json
{"timestamp": "2026-06-09T02:00:00Z", "event_id": 4624, "user": "ejike", "action": "LogonSuccess", "source_ip": "192.168.1.10"}
{"timestamp": "2026-06-09T02:05:00Z", "event_id": 4625, "user": "unknown", "action": "LogonFailure", "source_ip": "203.0.113.45"}

```

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
└───────────────┬───────────────┘
                │
┌───────────────┴───────────────┐
│   SOC Playbooks (Markdown)     │
│   (IR template + 4 scenarios)  │
└───────────────┬───────────────┘
                │
┌───────────────┴───────────────┐
│   Configs & Tests (Future)     │
│   (Splunk queries, unit tests) │
└───────────────────────────────┘

```

### 📊 Workflow Diagram (Mermaid)
### Repository Workflow
```mermaid
flowchart TD
    A[SIEM Log Parser (Python)] --> B[Event Parser (PowerShell)]
    B --> C[SSH Filter (Bash)]
    C --> D[MITRE ATT&CK Mapper (Python)]
    D --> E[Output Datasets (sample.log, mapped_logs.csv)]
    E --> F[SOC Playbooks (Markdown)]
    F --> G[Configs (Splunk queries, SIEM integrations)]
    G --> H[Tests (Unit tests for scripts)]

```
### Incident Response Lifecycle
```mermaid
flowchart TD
    Alert --> Triage --> Escalation --> Containment --> Eradication --> Recovery --> Lessons


---
### 👨‍💻 Contribution Guidelines  
- Fork the repo, create a feature branch, submit a pull request.
### 📜 Commit Message Convention
This project follows the [Conventional Commits](https://www.conventionalcommits.org/) standard:

#### Common Types
- `feat:` new feature (scripts, playbooks)
- `fix:` bug fix
- `docs:` documentation changes (README, playbooks, templates)
- `style:` formatting, whitespace, linting
- `refactor:` code restructuring without changing functionality
- `test:` adding or updating tests
- `chore:` maintenance tasks (dependencies, configs)

#### Examples
- `docs: add phishing email playbook`
- `feat(scripts): add MITRE ATT&CK mapper`
- `fix(scripts): correct log parser output format`
- `chore: update .gitignore for datasets`

### 📖 Documentation
Additional SOC workflow details and templates are available in the [docs folder](https://github.com/ennduka86-spec/SIEM-Log-Parsing-Scripts/tree/main/Scripts/docs).

- [Incident Response Template](https://github.com/ennduka86-spec/SIEM-Log-Parsing-Scripts/blob/main/Scripts/docs/incident_response_template.md) → step‑by‑step guide for handling alerts, triage, escalation, and recovery.  
- [SSH Failed Login Playbook](https://github.com/ennduka86-spec/SIEM-Log-Parsing-Scripts/blob/main/Scripts/docs/ssh_failed_login_playbook.md) → workflow for investigating repeated failed SSH logins.  
- [Suspicious Logon Playbook](https://github.com/ennduka86-spec/SIEM-Log-Parsing-Scripts/blob/main/Scripts/docs/suspicious_logon_playbook.md) → workflow for investigating unusual logon activity.  
- [Malware Infection Playbook](https://github.com/ennduka86-spec/SIEM-Log-Parsing-Scripts/blob/main/Scripts/docs/malware_infection_playbook.md) → workflow for investigating and remediating malware infections.  
- [Phishing Email Playbook](https://github.com/ennduka86-spec/SIEM-Log-Parsing-Scripts/blob/main/Scripts/docs/phishing_email_playbook.md) → workflow for investigating and responding to phishing attempts.  


### 📜 License
- MIT License — free to use and adapt with attribution.
