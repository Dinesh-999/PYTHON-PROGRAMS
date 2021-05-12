# Word count
s = "In this python project for beginners, the user has to click on a button which functions the user wants to access " \
    "eg – To edit a contact, the user has to first select a contact then click on view button then edit the contact " \
    "and then click on edit button. To add a new contact user has to click on the add button. "
print(f"Length of a string(in letters) or paragraph is : {len(s)}\n")
st = s.split(" ")
print(f"The words in the given string(in words) or paragraph is : \n{st}\n")
print(f"Length of a string(in words) or paragraph is : {len(st)}\n")

# multiline sentence
s1 = '''
sjgk
hkgl, dgkhj, ghhk
sksk
'''
s2 = s1.split()
print(len(s2))
