import csv
import os
import shutil


def create_sample_log(filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("2026-05-26,INFO,System started successfully.\n")
            file.write("2026-05-26,WARNING,Low disk space on drive C.\n")
            file.write("2026-05-26,ERROR,Database connection failed.\n")
        print(f"[SUCCESS] Sample file '{filename}' created.")
    except IOError as e:
        print(f"[ERROR] Could not write to {filename}: {e}")


def convert_log_to_csv(txt_filename, csv_filename):
    try:
        with open(txt_filename, "r", encoding="utf-8") as txt_file:
            lines = txt_file.readlines()

        with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Date", "Level", "Message"])

            for line in lines:
                row_data = line.strip().split(",")
                if len(row_data) == 3:
                    writer.writerow(row_data)

        print(f"[SUCCESS] Data converted and saved to '{csv_filename}'.")

    except FileNotFoundError:
        print(f"[ERROR] The source file '{txt_filename}' was not found.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred during conversion: {e}")


def automate_file_management(csv_file):
    try:
        archive_dir = "Archive_Folder"
        new_csv_name = "structured_report.csv"

        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)
            print(f"[AUTOMATION] Directory '{archive_dir}' created.")

        os.rename(csv_file, new_csv_name)
        print(f"[AUTOMATION] Renamed '{csv_file}' to '{new_csv_name}'.")

        destination_path = os.path.join(archive_dir, new_csv_name)
        shutil.move(new_csv_name, destination_path)
        print(f"[AUTOMATION] Moved '{new_csv_name}' to '{destination_path}'.")

    except FileNotFoundError:
        print("[ERROR] Automation failed: File to modify could not be located.")
    except PermissionError:
        print(
            "[ERROR] Automation failed: Insufficient permissions to modify files."
        )
    except Exception as e:
        print(f"[ERROR] Automation failed: {e}")


def cleanup_temp_files(txt_file):
    try:
        if os.path.exists(txt_file):
            os.remove(txt_file)
            print(f"[CLEANUP] Deleted original temp file '{txt_file}'.")
    except Exception as e:
        print(f"[ERROR] Cleanup failed: {e}")


if __name__ == "__main__":
    sample_txt = "raw_logs.txt"
    output_csv = "processed_logs.csv"

    print("--- Starting File Handling & Automation Script ---\n")

    create_sample_log(sample_txt)
    convert_log_to_csv(sample_txt, output_csv)
    automate_file_management(output_csv)
    cleanup_temp_files(sample_txt)

    print("\n--- Script Finished Successfully ---")