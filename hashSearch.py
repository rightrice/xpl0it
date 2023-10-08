import subprocess

input_file_path = "trialsAndTribulations.txt"
search_string = input("Enter the hash you want to search for: ")
worldOfOysters = ["hashcat", "arg1", "arg2", "arg3"]

with open(input_file_path, "r") as input_file:
    lines = input_file.readlines()
    matching_lines = []
    matching_found = False

    for i, line in enumerate(lines, start=1):
        if search_string in line:
            print("Matching line at line {}: {}".format(i, line.strip()))
            matching_found = True

if not matching_found:
    print("Sorry, we dont currently have that hash. We will begin work on that hash.")
    try:
        result = subprocess.run(worldOfOysters, stdout=subprocess.PIPE, stdder=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("The system is now beginning work on the Hash.")
            print(f"Hash Value: {result.stdout}")
        else:
            print("Sorry, the system couldn't do work to this hash.")

    except Exception as e:
        print("An error occured: ", str(e))