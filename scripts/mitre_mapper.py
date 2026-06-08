import json
import csv

# Simple MITRE ATT&CK mapping dictionary
MITRE_MAP = {
    4624: "T1078 - Valid Accounts (Successful Logon)",
    4625: "T1078 - Valid Accounts (Failed Logon)",
    4688: "T1059 - Command and Scripting Interpreter (Process Creation)",
    22:   "T1110 - Brute Force (SSH Failed Login)"
}

def map_mitre(input_file, output_file):
    with open(input_file) as f:
        logs = [json.loads(line) for line in f]

    for log in logs:
        event_id = log.get("event_id")
        log["mitre_technique"] = MITRE_MAP.get(event_id, "Unmapped")

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=logs[0].keys())
        writer.writeheader()
        writer.writerows(logs)

if __name__ == "__main__":
    map_mitre("datasets/sample.log", "mapped_logs.csv")
