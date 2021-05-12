# hangman program
# create a wordlist.txt file with some words

"""
import random
with open('wordlist.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]
"""

word = "Dinesh"
allowed_errors = 8
guesses = []
done = False

while not done:
    for letter in word.lower():
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print("")
    guess = input(f"Allowed errors left {allowed_errors}, next guess: ")
    guesses.append(guess.lower())
    # print(guesses)

    allowed_errors -= 1
    if allowed_errors == 0:
        break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found! the word. it is '{word}'")

else:
    print(f"Game over!. the word was '{word}'")
