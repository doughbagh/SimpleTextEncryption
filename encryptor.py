# Packages
import random
import string

# Variables
chars = " " + string.punctuation + string.digits + string.ascii_letters #Importing characters as a string to chars variable
chars = list(chars) # Making a chars variable into a list, to display each character individualy
key = chars.copy() # Copy chars data into a key variable
loop = True

while loop:
    random.shuffle(key) # Shuffling key characters into random order

    # print(f"chars): {chars}") - Used for testing
    # print(f"key): {key}") - Used for testing

    #ENCRYPTION
    plain_text = input("Enter your message: ")
    cipher_text = ""

    for letter in plain_text: # Iterate through each character in the encrypted message
        index = chars.index(letter) # Find the index of the current letter in the 'chars' list
        cipher_text += key[index] # Use the index to get the corresponding character from 'key' and add it to 'cipher_text'

    # Display the original and encrypted messages
    print(f"Original Message: {plain_text}")
    print(f"Encrypted Message: {cipher_text}")

    #DECRYPTION
    cipher_text_text = input("Enter your message to encrypt: ")
    plain_text = ""

    for letter in cipher_text: # Iterate through each character in the encrypted message
        index = key.index(letter) # Find the position of the current letter in the 'key' list
        plain_text += chars[index] # Use this index to find the corresponding character in 'chars' and add it to 'plain_text'

    # Display the original and encrypted messages
    print(f"Original Message: {plain_text}")
    print(f"Encrypted Message: {cipher_text}")
    ende = input("Do you want to encrypt and decrypt more text? (Yes/No): ").lower() # Ask if the user wants to continue with another encryption/decryption

    # Control flow to either continue the loop or break out of it
    if ende == "yes":
        continue
    else:
        break

