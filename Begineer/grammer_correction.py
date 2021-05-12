# Grammar Correction using Python
# internet connection is required to run this program

from gingerit.gingerit import GingerIt

text = input("Enter a sentence >>: ")
corrected_text = GingerIt().parse(text)
print(corrected_text)  # entire text
print(corrected_text['result'])  # only required result

# Enter a sentence >>: My name is Aman Kharwal, I will went to university tomorrow.
# My name is Aman Kharwal, I will go to university tomorrow.  (output)
