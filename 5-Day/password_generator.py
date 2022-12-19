#!/usr/bin/env python3

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
easy_or_hard = input("Choose rate of radomization? ('Easy' or 'Hard')\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
password_list = []
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
if easy_or_hard.lower() == "hard":
    #very random
    password_list.extend(random.choices(letters,k=nr_letters))
    password_list.extend(random.choices(numbers,k=nr_numbers))
    password_list.extend(random.choices(symbols,k=nr_symbols))
    random.shuffle(password_list)

    for elem in password_list:
        password += elem

else:
    # Just concat of sequence
    password_list.extend(random.choices(letters,k=nr_letters))
    password_list.extend(random.choices(numbers,k=nr_numbers))
    password_list.extend(random.choices(symbols,k=nr_symbols))

    for elem in password_list:
        password += elem

print(f"Generated password: {password}")
print(password_list)
