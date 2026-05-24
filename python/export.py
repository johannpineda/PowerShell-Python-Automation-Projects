import csv

def export_csv(logs):
    with open("output/logs.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["event", "user"])
        writer.writeheader()
        writer.writerows(logs)


def export_pdf(logs):
    # simple text-based PDF replacement (no external libs required)
    with open("output/logs.pdf", "w") as f:
        f.write("IT SYSTEM LOG REPORT\n\n")

        for log in logs:
            f.write(f"{log['event']} - {log['user']}\n")