import random

# Number guessing, numbers from 0 to 10

while True:
    num = random.randint(1, 10)
    # print(num)
    if num == 5 or num == 10:
        print("HINT: Number is Divisible by 5")

    elif num == 3 or num == 6 or num == 9:
        print("HINT: Number is multiple 3")

    elif num == 2 or num == 4 or num == 6 or num == 8:
        print("HINT: Number is even")

    else:
        print("HINT: Number is odd")

    user = int(input("Guess the number less than 10 : "))
    if num == user:
        print("YES. You guessed,👌 number is correct")
        break

    else:
        print("Try again...")

