import random

print("\nWelcome to PyPassword Generator!\n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_choice = int(input("How many letters would you like in your password? "))

sym_choice = int(input("\nHow many symbols would you like? "))
num_choice = int(input("\nHow many numbers would you like? "))

password = ""

for idx in range(1,letters_choice+1):
  password += letters[random.randint(0, len(letters)-1)]

for idx in range(1, sym_choice+1):
  password += symbols[random.randint(0, len(symbols)-1)]

for idx in range(1, num_choice+1):
  password += numbers[random.randint(0, len(numbers)-1)]

print(f"\nHere is your password: {password}")