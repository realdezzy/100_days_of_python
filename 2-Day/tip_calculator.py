#!/usr/bin/env python3

print("Welcome to the tip calculator.\n")
total = float(input("What was the total bill? "))
people = float(input("\nHow many people to split the bill? "))
tip = float(input("\nWhat percentage tip would you like to give? (10,12 or 15)? "))

tip_percentage = (total * tip) / 100
total_and_tip = total + tip_percentage
each_person_fee = total_and_tip / people

print("Each person should pay: ${:.2f}".format(each_person_fee))

