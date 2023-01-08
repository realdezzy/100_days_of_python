#!/usr/bin/python3
import string

print("Encode or decode text using ceasar cipher")

alphabet = {1:"a", 2:"b", 3:"c", 4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",
            10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",
            18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
user_input = input("Enter text to be encoded: ")
number_input = int(input("Enter the amount of times you want it shifted: "))

def encode(text, shifts):
    temp = ""

    for x in text:
        if (ord(x.lower()) < 97 or ord(x.lower()) > 122):
            temp += x
            continue
        char = ord(x.lower()) - 97
        shift = (char + shifts) % 26
        temp += string.ascii_lowercase[shift]

    print(temp)
    return temp
encoded_text = encode(user_input, number_input)

def decode(text, shifts):
    temp = ""

    for x in text:
        if (ord(x.lower()) < 97 or ord(x.lower()) > 122):
            temp += x
            continue
        char = ord(x.lower()) - 97
        shift = (char - shifts) % 26
        temp += string.ascii_lowercase[shift]

    print(temp)

decoded_text = decode(encoded_text, number_input)
