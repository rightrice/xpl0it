import hashlib
import os
from signatures import malware_signatures
from killswitch import secure_quarantine
import plyer
from plyer import notification


def calculate_file_hash(file_path):
    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
            file_hash = hashlib.md5(file_content).hexdigest()
            return file_hash
    except FileNotFoundError:
        return None
    
def scan_file(file_path):
    file_hash = calculate_file_hash(file_path)
    if file_hash:
        if file_hash in malware_signatures.values():
            print(f"Malware detected! The infected file is: {file_path}.")
            ## this is where I add quarantine and have y/n prompt to kill file

            ## desktop notification cause we boujee
            notification.notify(
                title="Malware Detected!",
                message="Please check XPL0IT to determine what to do with the malware.",
                app_name="Name",
                ticker="test",
                ##  app_icon="test.ico",
                timeout=7
            )
        else:
            print(f"No malware was detected in this file: {file_path}.")
            ## y/n prompt to search another file
            ## input("Please type your next file path...")
            ## notification
            notification.notify(
                title="No Malware Detected!",
                message="You may scan another file or exit the program safely.",
                app_name="Name",
                ticker="test",
                ##  app_icon="test.ico",
                timeout=7
            )
    else:
        print(f"File not found: {file_path}.")
        notification.notify(
            title="No File Found!",
            message="Please check your file path and try again.",
            app_name="Name",
            ticker="test",
            ##  app_icon="test.ico",
            timeout=7
        )

def scan_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_file_hash(file_path)

            if file_hash:
                if file_hash in malware_signatures.values():
                    print(f"Malware detected! The infected file(s) in this directory are: {directory_path}")
                    ## This is where I add quarantine and have y/n prompt to kill directory
                else:
                    print(f"No malware was detected in directory: {directory_path}")
            else:
                print(f"Directory not found: {directory_path}")