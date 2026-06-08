# SOC Playbook: Failed SSH Login Investigation

## Objective
Investigate repeated failed SSH login attempts to detect brute force or unauthorized access.

## Steps

### 1. Detection
- SIEM alert triggered for multiple failed SSH logins.
- Review source IP, username, and timestamps.

### 2. Triage
- Validate if attempts are legitimate (e.g., admin mistyping password).
- Check frequency and distribution of failures.

### 3. Escalation
- If suspicious, escalate to Tier 2 SOC analyst.
- Enrich with threat intel (IP reputation, geolocation).

### 4. Containment
- Block offending IPs at firewall.
- Disable targeted accounts if compromised.

### 5. Eradication
- Remove unauthorized keys or accounts.
- Patch SSH configuration vulnerabilities.

### 6. Recovery
- Restore normal access for valid users.
- Monitor for recurrence.

### 7. Lessons Learned
- Update detection rules for brute force attempts.
- Add MFA for SSH access.
