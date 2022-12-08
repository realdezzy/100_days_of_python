#!/usr/bin/env python3

height = input("Enter your height in m: ")
weight = input("\nEnter your weight in kg: ")

bmi = float(weight) / (float(height) ** 2)

print("\nYour body mass index is: {:d}".format(int(bmi)))
