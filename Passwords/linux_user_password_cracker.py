#!/usr/bin/python3
import crypt
import sys

# Hash extracted from /etc/shadow.txt
entry = "$6$bVtoNJr/GHPs7R$i7Ip5frU9wEfPfGhFGE2w6CkdTpL21zQ2zRbZyR51KkFilzOf8prHxhxpiDzuxRhS8/TZyQ04t25hDXOajIl7."

password_found = False

# Loop thought the dictionary to find the password
with open("../Data/dictionary") as file:
    for line in file:
        word = line.strip()

        hash = crypt.crypt(word, "$6$bVtoNJr/GHPs7R$")

        if hash == entry:
            print("Password found: {}".format(word))
            password_found = True
            break
        else:
            password_found = False


# If Password was not found it terminate with a string
if not password_found:
    print("Password was not found")

print("Programm finished")
sys.exit()