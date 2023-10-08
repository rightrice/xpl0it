input_file_path = "trialsAndTribulations.txt"
search_string = input("Enter the hash you want to search for: ")

with open(input_file_path, "r") as input_file:
    lines = input_file.readlines()
    matching_lines = []
    matching_found = False

    for i, line in enumerate(lines, start=1):
        if search_string in line:
            print("Matching line at line {}: {}".format(i, line.strip()))
            matching_found = True

if not matching_found:
    print("Sorry, we dont currently have that hash. We will work to add it.")