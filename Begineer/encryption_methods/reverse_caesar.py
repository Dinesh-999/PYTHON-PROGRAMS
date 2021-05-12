# Caesar Cipher Algorithm reversing  [decoding]
# Brute Force Technique

message = 'GIEWIV GMTLIV HIQS'  # encrypted message  # correct key value is 4
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol

    print('Hacking key #%s: %s' % (key, translated))
