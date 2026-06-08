# SOC Playbook: Suspicious Logon Activity

## Objective
Investigate unusual logon events that may indicate compromised credentials.

## Steps

### 1. Detection
- SIEM alert triggered for logon outside business hours or from unusual location.

### 2. Triage
- Validate user activity against HR/work schedule.
- Check device, IP, and geolocation.

### 3. Escalation
- Escalate if logon is inconsistent with user profile.
- Enrich with threat intel (IP reputation, device fingerprint).

### 4. Containment
- Force password reset.
- Lock account if compromise suspected.

### 5. Eradication
- Remove malicious persistence mechanisms.
- Patch exploited vulnerabilities.

### 6. Recovery
- Restore account access after verification.
- Monitor for abnormal activity.

### 7. Lessons Learned
- Update detection rules for anomalous logons.
- Implement conditional access policies.
