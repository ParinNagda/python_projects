import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: \n").upper()
    try:
        word_list = [phonetic_dict[letter] for letter in word]
    except KeyError as error:
        print("Please use letters in alphabet")
        generate_phonetic()
    else:
        print(word_list)
