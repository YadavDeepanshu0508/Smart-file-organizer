from scanner import scan_folder
from duplicate_detector import find_duplicates
# pyrefly: ignore [missing-import]
from organizer import organize_files
from report_generator import generate_report

folder = input("Enter folder path: ")

files = scan_folder(folder)

duplicates = find_duplicates(files)

organize_files(files)

generate_report(files, duplicates)

print("Analysis Complete!")