import sys


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    try:
        archivist_id = input("Input Stream active. Enter archivist ID: ")
        status_report = input("Input Stream active. Enter status report: ")

        sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: "
                         f" {status_report}")
        sys.stderr.write("\n[ALERT] System diagnostic: "
                         "Communication channels verified")
        sys.stdout.write("\n[STANDARD] Data transmission complete\n")

    except ValueError:
        sys.stdout.write("\nERROR: Wrong identification")

    finally:
        sys.stdout.write("\nThree-channel communication test successful.")
