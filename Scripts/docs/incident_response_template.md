# Incident Response Template

## 1. Alert
- SIEM generates an alert from raw logs.
- Document alert details: timestamp, source, severity, affected systems.

## 2. Triage
- Validate the alert (false positive vs true positive).
- Normalize logs for easier analysis.
- Assign priority based on impact.

## 3. Escalation
- Enrich logs with MITRE ATT&CK mapping.
- Decide if escalation to Tier 2/Threat Intel team is required.
- Record escalation details.

## 4. Containment
- Apply immediate controls (disable accounts, block IPs, isolate endpoints).
- Document containment actions taken.

## 5. Eradication
- Remove malicious files, registry entries, or unauthorized accounts.
- Patch vulnerabilities exploited.
- Confirm eradication steps.

## 6. Recovery
- Restore systems to operational state.
- Validate recovery with clean logs.
- Monitor for recurrence.

## 7. Lessons Learned
- Conduct post‑incident review.
- Update detection queries and playbooks.
- Feed insights back into detection engineering.

---
