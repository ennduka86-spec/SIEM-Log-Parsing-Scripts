import json, csv

def parse_log(input_file, output_file):
    with open(input_file) as f:
        logs = [json.loads(line) for line in f]
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=logs[0].keys())
        writer.writeheader()
        writer.writerows(logs)

parse_log("sample.log", "parsed_logs.csv")
