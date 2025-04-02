import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name!: ").upper()
print("\n")
output_list = [phonetic_dictionary[letter] for letter in name]
print(output_list)

