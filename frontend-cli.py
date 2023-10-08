## Dependencies and Modules
import os
import webbrowser
import hashlib
from signatures import malware_signatures
from zero import scan_file
from zero import scan_directory
website = "website.com"
database = "database.website"
##---------------------------------------------##
def main():
    print("Welcome to Project XPL0IT\n")
    while True:
        print("\nMenu:")
        print("\n1. Scan a File")
        print("\n2. Scan a Directory")
        print("\n3. Scan this PC")
        print("\n4. Search the Database")
        print("\n5. Quit")

        choice = input("\nWhat would you like to use Project XPL0IT for today?")
        if choice == "1":
            file_path = input("Enter the path for the file you'd like to scan: ")
            if os.path.exists(file_path):
                scanResult = scan_file(file_path)
                print("File Scan results: ", scanResult)
            else:
                print("Error: File not found.")
        elif choice == "2":
            directory_path = input("Enter the path for the directory you'd like to scan: ")
            if os.path.exists(directory_path):    
                scanResult = scan_directory(directory_path)
                print("Directory Scan results: ", scanResult)
            else:
                print("Error: Directory not found.")
        elif choice == "3":
            # Need to figure out how to scan an entire drive...that needs to be added to the zero.py file
            drive_path = input("Enter the letter for the drive you'd like to scan: ")
            if os.path.exists(drive_path):
 #               scanResult = scan_drive(drive_path)
                print("Drive scan results: ", scanResult)
        elif choice == "4":
            print("Opening the database...")
            webbrowser.open(database)
        elif choice == "5":
            print("Goodbye, see you again!")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()