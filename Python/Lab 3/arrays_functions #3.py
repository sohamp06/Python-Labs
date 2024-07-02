# PROGRAM NAME: arrays_functions
# PROGRAM AUTHOR: SOHAM PATEL
# DATE: March 25, 2023
# PROGRAM DESCRIPTION: Convert letters between english language and al bhed language


# ----------------------------------
# GOT SOME REFFERENCES FROM INTERNET 
# ----------------------------------
# variables
encrypted = 0
decrypted = 0

valid = True

while valid:
 # asking user for an input
 def print_options():
        # choose 1 to encrypt a message
        print("Press 1 for Encryption")
        # choose 2 to decrypt a message
        print("Press 2 for Decryption")
        # choose 3 to exit
        print("Press 3 to Exit")
# functions for encryptions
 def encrypt():
    # ask for input to encode a message
    input_message = input("Please enter the message you would like to encode. ")
    encrypted = ""
    for characters in input_message:
        # covert to al bhed language 
        encrypted += chr(ord(characters) + 1)
        # print an encoded message
        print("Encoded message: ",encrypted)
# functions for decryptions
 def decrypt():
    # ask for input to decode a message
    input_message = input("Please enter the message you would like to decode. ")
    decrypted = ""
    for characters in input_message:
        # convert to english language
        decrypted =chr(ord(characters) - 1)
        # print a decoded message
        print("Encoded message: ",decrypted)
# initial prompt to user
 print_options()
 # ask the user to enter a number they would like to execute
 select = input("Plese enter the number that you would ike to execute. ")
 # option 1
 if select == "1":
    encrypt()
# option 2
 elif select == "2":
    decrypt()
# option 3
 elif select == "3":
    break
 # print an message to must enter a number between 1 -3 
 else: 
    print("Enter between 1 - 3")
   







# DESK CHECH 1
# Press 1 for Encryption
# Press 2 for Decryption
# Press 3 to Exit
# Plese enter the number that you would ike to execute. 1
# Please enter the message you would like to encode. heLLO
# Encoded mesage: raMMU


# DESK CHECH 2
# Press 1 for Encryption
# Press 2 for Decryption
# Press 3 to Exit
# Plese enter the number that you would ike to execute. 2
# Please enter the message you would like to encode. Hela du saad oui 
# Encoded mesage: Nice to meet you