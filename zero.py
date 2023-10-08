import hashlib
import os
from signatures import malware_signatures
from killswitch import secure_quarantine

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
            ## This is where I add quarantine and have y/n prompt to kill file
        else:
            print(f"No malware was detected in this file: {file_path}.")
            ## y/n prompt to search another file
    else:
        print(f"File not found: {file_path}.")

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