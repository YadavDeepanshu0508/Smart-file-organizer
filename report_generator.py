import os

def generate_report(files, duplicates):

    report_path = os.path.join(
        os.path.dirname(__file__),
        "report.txt"
    )

    total_size = 0

    for file in files:
        try:
            total_size += os.path.getsize(file)
        except:
            pass

    with open(report_path, "w") as f:

        f.write("SMART FILE ORGANIZER REPORT\n")
        f.write("=" * 40 + "\n")

        f.write(f"Total Files: {len(files)}\n")
        f.write(f"Duplicates Found: {len(duplicates)}\n")
        f.write(f"Total Storage: {total_size / 1024 / 1024:.2f} MB\n")

    print("Report Created!")