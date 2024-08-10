import pandas as pd
#TODO 1. Create a dictionary in this format:
data = pd.read_csv('nato_phonetic_alphabet.csv')

NATO_dict = {row.letter:row.code for (index,row) in data.iterrows()}




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = str(input('What is your name?')).upper()
code = [NATO_dict[letter] for letter in name]
print(code)
