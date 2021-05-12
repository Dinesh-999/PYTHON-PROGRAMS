# printing colored text

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(Fore.BLUE + Back.YELLOW + "Hi My name is Aman Kharwal " + Fore.YELLOW + Back.BLUE + "I am your Machine Learning Instructor")
print(Back.CYAN + "Hi My name is Aman Kharwal")
print(Fore.RED + Back.GREEN + "Hi My name is Aman Kharwal")

# 2nd type to print coloured text

from termcolor import colored
print("\n")
print(colored('Hello, World!', 'green', 'on_red'))
print(colored('Hello, World!', 'green'))
