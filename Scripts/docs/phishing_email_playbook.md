# SOC Playbook: Phishing Email Investigation

## Objective
Investigate and respond to suspected phishing emails reported by users or detected by SIEM/email security tools.

## Steps

### 1. Detection
- SIEM/email gateway alert triggered for suspicious email.
- User reports suspicious email to SOC.
- Collect email metadata: sender, subject, attachments, URLs.

### 2. Triage
- Validate if email is malicious (check headers, SPF/DKIM records).
- Analyze links and attachments in a sandbox.
- Assess scope: single user vs multiple recipients.

### 3. Escalation
- Escalate to Tier 2 SOC analyst if phishing confirmed.
- Enrich with threat intel (malicious domains, known phishing campaigns).
- Document escalation details.

### 4. Containment
- Block sender domain/IP in email gateway.
- Quarantine malicious emails across mailboxes.
- Disable compromised accounts if credentials harvested.

### 5. Eradication
- Remove phishing emails from affected inboxes.
- Delete malicious attachments or links.
- Patch exploited vulnerabilities in email systems.

### 6. Recovery
- Restore normal email operations.
- Reset passwords for affected users.
- Monitor for follow‑up phishing attempts.

### 7. Lessons Learned
- Conduct awareness training for users.
- Update detection rules for phishing indicators.
- Improve reporting workflows for suspicious emails.
