#!/usr/bin/env python3

print("Welcome to top secret auction")

max_bidder = ""
max_bid = 0
while True:
    name = input("What's your name?: ")
    bid = int(input("\nWhat's your bid?: $"))

    if (bid > max_bid):
        max_bid = bid
        max_bidder = name
    last = input("\nAre there any bidders left? (Yes or No): ")
    if last.lower() == "no":
        break

print(f"The winner is {max_bidder} with a bid of ${max_bid}") 

