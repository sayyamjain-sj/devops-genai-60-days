from pathlib import Path
import json


LOG_FILE = Path("sample.log")
REPORT_FILE = Path("log_report.json")


def analyze_log(log_file):
    info_count = 0
    warning_count = 0
    error_count = 0

    error_messages = []
    error_types = {}

    try:
        with log_file.open("r") as file:
            for line in file:
                line = line.strip()

                if "ERROR" in line:
                    error_count += 1

                    # Save complete error line
                    error_messages.append(line)

                    # Extract only the message after the word ERROR
                    message = line.split("ERROR", 1)[1].strip()

                    # Count duplicate error messages
                    if message in error_types:
                        error_types[message] += 1
                    else:
                        error_types[message] = 1

                elif "WARNING" in line:
                    warning_count += 1

                elif "INFO" in line:
                    info_count += 1

    except FileNotFoundError:
        print(f"ERROR: File '{log_file}' was not found.")
        return None

    report = {
        "info": info_count,
        "warnings": warning_count,
        "errors": error_count,
        "error_messages": error_messages,
        "error_types": error_types
    }

    return report


def print_report(report):
    if report is None:
        return

    print("\nLOG REPORT")
    print("=" * 30)

    print(f"INFO: {report['info']}")
    print(f"WARNING: {report['warnings']}")
    print(f"ERROR: {report['errors']}")

    print("\nErrors found:")

    if report["error_messages"]:
        for error in report["error_messages"]:
            print(error)
    else:
        print("No errors found.")

    print("\nError breakdown:")

    if report["error_types"]:
        for error, count in report["error_types"].items():
            print(f"{error}: {count}")
    else:
        print("No error types found.")


def save_report(report, report_file):
    if report is None:
        return

    try:
        with report_file.open("w") as file:
            json.dump(report, file, indent=4)

        print(f"\nReport saved to: {report_file}")

    except OSError as error:
        print(f"ERROR: Could not save report.")
        print(error)


if __name__ == "__main__":
    report = analyze_log(LOG_FILE)

    print_report(report)

    save_report(report, REPORT_FILE)