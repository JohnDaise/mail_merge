# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import shutil

SOURCE_PATH = "./Input/Letters/starting_letter.txt"
DESTINATION_PATH = "./Output/ReadyToSend/"
PLACEHOLDER = "[name]"

names_file = open("./Input/Names/invited_names.txt", "r")
names = names_file.readlines()

for name in names:
    new_file_name_path = DESTINATION_PATH + name + "_invite.txt"
    with open(SOURCE_PATH, 'r') as open_file, open(new_file_name_path, 'w') as write_file:
        for line in open_file:
            new_line = line.replace(PLACEHOLDER, name.strip(), 1)
            write_file.write(new_line)


    # create file
    # get letter from starting letter
    # replace name in letter
    # add to ReadytoSend





