#!/usr/bin/env python3

import random

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  \n''')
#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
                    'coyote crow deer dog donkey duck eagle ferret fox frog goat '
                    'goose hawk lion lizard llama mole monkey moose mouse mule newt '
                    'otter owl panda parrot pigeon python rabbit ram rat raven '
                    'rhino salmon seal shark sheep skunk sloth snake spider '
                    'stork swan tiger toad trout turkey turtle weasel whale wolf '
                    'wombat zebra ').split()
word = random.choice(words)
hangman_gallows = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def print_list(listt):
    for i in listt:
        print(i,end=" ")
    print()

word_list = []
gallow = hangman_gallows[0]
count = 0
life = 0

for _ in word:
    word_list += "_"
choice = input("Guess a letter: ")

while True:
    if choice in word:
        for pos in range(len(word)):
            if choice == word[pos]:
                if choice not in word_list:
                    count += 1
                word_list[pos] = choice
        print("\033c\033[3J", end='')
        print_list(word_list)
        print()
        print('\r' + gallow)
    else:
        life += 1
        gallow = hangman_gallows[life]
        print("\033c\033[3J", end='')
        print_list(word_list)
        print(f"You guessed {choice}, that's not in the word. You lose a life.")
        print('\r' + gallow)
        if life == len(hangman_gallows) - 1:
            print("Failed")
            break

    if count == len(word):
        print("You won")
        break
    choice = input("Guess a letter: ")

