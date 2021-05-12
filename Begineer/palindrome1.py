# searches palindrome in a sentences
# LOL, My interview went good. My Mom will be so happy.  , enter this sentence in input

def palindrome(sentence):
    for i in ",.'?/><}{{}}'":
        sentence = sentence.replace(i, "")
    palindrome = []
    words = sentence.split(' ')
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    return palindrome


sentence = input("Enter a sentence : ")
print(palindrome(sentence))

