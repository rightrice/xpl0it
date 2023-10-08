import hashlib

algorithm_choice = input("What hash would you like to generate?\nYou can type an algorithm like: sha256 or md5.\n")
user_input = input("Enter the string to hash: ")

if algorithm_choice == "md5":
    hash_object = hashlib.md5()
elif algorithm_choice == "sha1":
    hash_object = hashlib.sha1()
elif algorithm_choice == "sha256":
    hash_object = hashlib.sha256()
elif algorithm_choice == "sha512":
    hash_object = hashlib.sha512()
elif algorithm_choice == "sha3256":
    hash_object = hashlib.sha3_256()
elif algorithm_choice == "sha3512":
    hash_object = hashlib.sha3_512()
else:
    print("Sorry, that is an invalid algorithm choice. Please try again.")
    exit(1)

hash_object.update(user_input.encode())
hashed_value = hash_object.hexdigest()

print(f"{algorithm_choice.upper()} hash:", hashed_value)

with open("trialsAndTribulations.txt", "a") as file:
    file.write(f"\n{hashed_value}:{user_input}")