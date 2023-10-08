## Dependencies and Modules
import os
import sys
import webbrowser
import hashlib
from signatures import malware_signatures
from zero import scan_file
from zero import scan_directory
from time import sleep
from typing import Tuple
website = "website.com"
database = "database.website"
## clear terminal
os.system('cls')
## Typewriter affect
DELAY: float = .1
def cc(*paragraph:str) -> None:
    for sentence in paragraph:
        for char in sentence:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(DELAY)
        print()
        sleep(DELAY)
##---------------------------------------------##
def main():
    cc("Welcome to Project XPL0IT\n")
    while True:
        cc("\nMenu:")
        cc("\n1. Scan a File")
        cc("\n2. Scan a Directory")
        cc("\n3. Scan this PC")
        cc("\n4. Search the Database")
        cc("\n5. Quit")

        choice = input("\nWhat would you like to use Project XPL0IT for today? ")
        if choice == "1":
            file_path = input("Enter the path for the file you'd like to scan: ")
            if os.path.exists(file_path):
                scanResult = scan_file(file_path)
                cc("File Scan results: ", scanResult)
            else:
                cc("Error: File not found.")
        elif choice == "2":
            directory_path = input("Enter the path for the directory you'd like to scan: ")
            if os.path.exists(directory_path):    
                scanResult = scan_directory(directory_path)
                cc("Directory Scan results: ", scanResult)
            else:
                cc("Error: Directory not found.")
        elif choice == "3":
            # Need to figure out how to scan an entire drive...that needs to be added to the zero.py file
            drive_path = input("Enter the letter for the drive you'd like to scan: ")
            if os.path.exists(drive_path):
 #               scanResult = scan_drive(drive_path)
                cc("Drive scan results: ", scanResult)
        elif choice == "4":
            cc("Opening the database...")
            webbrowser.open(database)
        elif choice == "5":
            cc("Goodbye, see you again!")
            break
        else:
            cc("Invalid selection, please try again.")

if __name__ == "__main__":
    main()