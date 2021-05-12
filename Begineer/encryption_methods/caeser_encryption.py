# simple caeser_encryption
# neuralnine

import string
import stringprep

plain_text = "hello world"  # for encryption
# plain_text = "jgnnq yqtnf"  # for decryption

shift = 2  # shift for encryption
# shift = 26-2   # for decryption
# shift = shift % 26    # for decryption

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)
print(encrypted)

""" 
# function for encryption
def caeser(text, shift, alphabets):
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = "".join(alphabets)
    final_alphabet_alphabet = "".join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_alphabet_alphabet)
    return text.translate(table)


plain_text = "This is a new test. Hello World!"
print(caeser(plain_text, 7, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))

"""
