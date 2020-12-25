# Code for Day 24 Project.

# TODO: Create a letter using starting_letter.docx 
# for each name in invited_names.txt

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open('Day 24 - Intermediate - Files, Directories and Paths/Mail Merge/Input/Names/invited_names.txt', 'r') as file:
    names = file.read()

with open('Day 24 - Intermediate - Files, Directories and Paths/Mail Merge/Input/Letters/starting_letter.docx', 'r') as file:
    letter = file.read()

for name in names.split():

    new_letter = letter
    new_letter = new_letter.replace('[name]', name)

    with open(f'Day 24 - Intermediate - Files, Directories and Paths/Mail Merge/Output/Letters/letter_for_{name}.docx', 'w') as file:
        file.write(new_letter)
