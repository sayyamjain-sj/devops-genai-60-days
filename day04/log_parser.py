from pathlib import Path
import json

LOG_FILE = Path("sample.log")
REPORT_FILE = Path("log_report.json")


def analyze_log():
    errors = 0
    warnings = 0
    info = 0

    error_messages = []
    error_types = {}

    try:
        with LOG_FILE.open("r") as file:
            lines = file.readlines()

            for line in file:

                if "ERROR" in line:
                    errors += 1

                    # Save complete error line
                    error_messages.append(line.strip())

                    # Extract only the error message
                    message = line.split("ERROR", 1)[1].strip()

                    # Count duplicate error types
                    if message in error_types:
                        error_types[message] += 1
                    else:
                        error_types[message] = 1

                elif "WARNING" in line:
                    warnings += 1

                elif "INFO" in line:
                    info += 1

    except FileNotFoundError:
        print(f"ERROR: {LOG_FILE} was not found.")
        return

    # Display summary
    print("LOG REPORT")
    print("=" * 30)
    print(f"INFO: {info}")
    print(f"WARNING: {warnings}")
    print(f"ERROR: {errors}")

    print("\nErrors found:")

    for message in error_messages:
        print(message)

    print("\nError breakdown:")

    for error, count in error_types.items():
        print(f"{error}: {count}")

    # Create structured report
    report = {
        "info": info,
        "warnings": warnings,
        "errors": errors,
        "error_types": error_types
    }

    # Save report as JSON
    with REPORT_FILE.open("w") as file:
        json.dump(report, file, indent=4)

    print(f"\nJSON report created: {REPORT_FILE}")


if __name__ == "__main__":
    analyze_log()