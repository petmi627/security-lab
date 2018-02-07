# This Script test if a given md5 hash matched with an entry in our dictionary
# If that's the case you the password in plain text.
# --help for more information
import sys
import os
import hashlib

# Parsing Arguments to Application
try:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dictionary", help="Enter the File path of the dictionary")
    parser.add_argument("--hash", help="Please enter the Hash value", type=str)
    flags = parser.parse_args()
except ImportError:
    flags = None

# If hash was not passed the Application quit with an error message
if flags.hash:
    hash = flags.hash
else :
    print("You need to enter a hash")
    sys.exit(1)

# If a dictionary is passed it take this one, otherwise it will take a default dictionary
if flags.dictionary:
    filepath = flags.dictionary
    if not os.path.isfile(filepath):
        print("File {} doesn't exists".format(filepath))
        sys.exit(1)
else:
    filepath = "../Data/dictionary.txt"
    print("No dictionary passed, reading default dictionary in '{}'.".format(filepath))
    if not os.path.isfile(filepath):
        print("File {} doesn't exists".format(filepath))
        sys.exit(1)


# Password Found variable is False
password_found = False


# Loop trought the dictionary file to find the hash
with open(filepath, "r") as file:
    for line in file:
        word = line.strip()

        if hashlib.md5(word.encode('utf-8')).hexdigest() == hash:
            password_found = True
            print("Password for hash {} found: {}".format(hash, word))
            break
        else:
            password_found = False


# If Password was not found it terminate with a string
if not password_found:
    print("Password was not found")

print("Programm finished")
sys.exit()