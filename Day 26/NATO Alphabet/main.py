import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

word = input("Enter a word: \n").upper()

word_list = [phonetic_dict[letter] for letter in word]

print(word_list)
