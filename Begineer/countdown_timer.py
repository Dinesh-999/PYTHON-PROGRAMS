# countdown timer

import time


def countdown(ti):
    while ti:
        mins, secs = divmod(ti, 60)
        timer = f'{mins} min, {secs} sec'
        print(timer, end="\n")
        time.sleep(1)
        ti -= 1

    print('Blast Off!!!')


t = input("Enter the time in seconds: ")
countdown(int(t))
