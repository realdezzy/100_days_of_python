#!/usr/bin/env python3
import random

print("Welcome to the Rock Paper Scissors game!")

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

artlist = [rock_art,paper_art,scissors_art]

try:

    user_choice = int(input("What do you want to choose?..\nType 0 for rock, 1 for Paper or 2 for Scissors.\n"))
    print(artlist[user_choice])

    comp_choice = random.randrange(0,3)
    print(f"Computer chose:\n {artlist[comp_choice]}")

    if user_choice == comp_choice:
        print("It's a draw")
    elif user_choice == 0 and comp_choice == 2:
        print("You win")
    elif user_choice == 1 and comp_choice == 0:
        print("You win")
    elif user_choice == 2 and comp_choice == 1:
        print("You win")
    else:
        print("You lose")

except Exception as e:
    print("Must pass integer value as input")
    print(e)
