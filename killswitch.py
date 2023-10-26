import os
import shutil
import hashlib

def secure_quarantine(file_path, quarantine_dir, hash_function):
    try:
        # XPL0IT checking if file exists
        if os.path.exists(file_path):
            # Creating quarantine directory if it isn't already created
            os.makedirs(quarantine_dir, exist_ok=True)

            # Creating new path for quarantined file
            quarantine_path = os.path.join(quarantine_dir, os.path.basename(file_path))

            # Making the SHA-256 hash for file
            file_hash = hash_function(file_path)

            # Renaming the quarantined file with .kill extension and also storing the hash in endeavour.txt
            quarantine_file_name = f"{os.path.basename(file_path)}.kill"
            quarantine_file_path = os.path.join(quarantine_dir, quarantine_file_name)

            # Moving the file to the quarantine directory
            shutil.move(file_path, quarantine_file_path)

            # Storing quarantined file's hash in endeavour.txt
            with open(os.path.join(quarantine_dir, "endeavour.txt"), "a") as hash_file:
                hash_file.write(f"{quarantine_file_name}: {file_hash}\n")

            print(f"File Quarantined: {file_path}")
        else:
            print(f"File not found: {file_path} ... no files quarantined.")
    except Exception as e:
        print(f"Failed to quarantine the file: {e}")

file_to_quarantine = ""
quarantine_dir = "/deadToRights"

def calculate_sha256_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536) # Reads in 64k chunks
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()
secure_quarantine(file_to_quarantine, quarantine_dir, calculate_sha256_hash)