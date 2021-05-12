# Caesar_cipher algorithm

def encrypt(text, s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
            # ord converts char to ascii value
            # chr converts ascii value to char

        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# check the above function
text = "CEASER CIPHER DEMO"  # u can try CEASER cipher DEMO
s = 4  # you can increase the value 1-25

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text, s))
