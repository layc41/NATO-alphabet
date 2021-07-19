import pandas

# Original Code
# nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# nato_letter = nato_data['letter'].to_list()
# nato_code = nato_data['code'].to_list()
# nato_dict = {nato_letter[i]: nato_code[i] for i in range(len(nato_letter))}
#
# user_input = input("Enter word: ").upper()
# phonetic_list = [nato_dict[letter] for letter in user_input if letter in nato_dict]
# print(phonetic_list)

# Cool Solution Code
# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Beta"...}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# turn every letter to uppercase because dictionary is uppercase
user_input = input("Enter word: ").upper()
phonetic_list = [nato_dict[letter] for letter in user_input if letter in nato_dict]
print(phonetic_list)
