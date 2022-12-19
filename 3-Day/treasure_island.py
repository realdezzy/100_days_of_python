#!/usr/bin/env python3

import time

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')


print("\nWelcome to Treasure Island.\nYour mission is to find the treasure.")

first_choice = input('\nYou\'re at a cross road.\nWhere do you want to go? Type "left" or "right" \n')
time.sleep(2)
print()

if (first_choice.lower() != "left"):
    print("Wrong turn, better luck next time :(")
    exit()
else:
    print("Right choice adventurer!, keep going")
time.sleep(2)
print(''' I
                                  Y
   |                              T                              |
  .'.                           .' '.                           .'.
 (__ )                        _;-----;_                        (__ )
  |A|                       .':::::    '.                       |A|
 .===.                     /:::::::      \                     .===.
 |/  |                |   ::::::::        :   |                |/  |
 |/  |      |       ,' ', |:::::::        | ,' ',       |      |/  |
 |/  |     ( )     (:.___)\:::____________/(:.___)     ( )     |/  |
 |===|      H    I  |(_)V__)-------------(__V(_)|  I    H      |===|
 |/  |     |=|   Y_.----|  _______________  |----._Y   |=|     |/  |
 |/  |     |:|   | | __ | [,-------------,] | __ | |   |:|     |/  |
 |/  |     |:|   | |/  \| [|    _.-._    |] |/  \| |   |:|     |/  | 
 |===|     |:|   |'||  || [|   /  '::\   |] ||  ||'|   |:|     |===|
 |/  |     |:|   |_||__|| []  |    :::|  [] ||__||_|   |:|     |/  |
 |/  |     |:|   | | __ | []  |    :::|  [] | __ | |   |:|     |/  |
 |/  |     |:|   |.|/  \| []  |    :::|  [] |/  \|.|   |:|     |/  |
 |/  |     |:|   | ||  || []  |     ::|  [] ||  || |   |:|     |/  |
 |/__|_____|:|___| ||__||_[]__|_____::|__[]_||__||_|___|:|_____|/__|
|/    |-------------------------------------------------------|/    |
|/    |                                                       |/    |
|/____|_________________________________________________snd___|/____|''')

print("\nYou just got to a beautiful building,Pause for a second and admire it's grandeur!")
time.sleep(1)
print("You have got to enter the building to search for the treasure")
print("But you have to choose between going through the front or back door")
building_choice = input('Choose "front" or "back"\n')

time.sleep(2)
print()

if (building_choice.lower() == "back"):
    print("Your instincts are superb")
elif (building_choice.lower() == "front"):
    print("The front door is boobytrapped, You got hit by a kunai to the throat")
    print("Gameover, but you can return from Valhalla and try again")
    exit()
else:
    print("Wrong input, start over")
    exit()
time.sleep(2)

print("Now you are in the house, you have to decide which floor to search")
print("Tip! the house has two floors")
floor = input("Choose which floor to search? ('1' or '2'): \n")
time.sleep(2)
if (floor == '1'):
    print("There are traps everywhere, and you got caught in one")
    print("Gameover,restart")
    exit()
elif (floor == '2'):
    print(flush=True)
    print("Congratulations you found the treasure!")
    print('''         _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | Linux Rules! |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' hjm''')
else:
    print("You triggered the alarms with a wrong input")
    print("Mission failed")
    exit()

