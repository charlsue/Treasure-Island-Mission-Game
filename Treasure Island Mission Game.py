print('''
*******************************************************************************
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
*******************************************************************************
''')
while True:
          print("Welcome to Treasure Island.")
          print("Your mission is to find the treasure.") 

#Write your code below this line 👇
          first_destination = input("You are at the crossroad. Where do you want to go? To the left where many theives are lurking or to the right where many wild animals? Type 'left' or 'right'\n")
          first_destination = first_destination.lower()
          if first_destination == "left":
                    try_again = input("You are dead. You are killed by the theives. Would you like to play again? Type 'yes' or 'no'\n")
                    try_again = try_again.lower()
                    if try_again == "yes":
                              print("\n\n\n")
                              continue
                              
                      
          else: 
                    second_destination = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat to come by or type 'swim' to swim across\n")
                    second_destination = second_destination.lower()
          if second_destination == "wait":
                    third_destination = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which on would you enter?\n")
                    third_destination = third_destination.lower()
          else:
                    print("You are dead. You are eaten by crocodiles. Game over")
                    try_again = input("Would you like to play again? Type 'yes' or 'no'\n")
                    if try_again == "yes":
                              print("\n\n\n")
                              continue
                             
                    
          if third_destination == "red":
                    print("Burned by fire. Game over")
          elif third_destination == "blue":
                    print("Eaten by beasts. Game over")
          elif third_destination == "yellow":
                    print("\n")
                    print("You win! You got a treasure full of golds! Congratulations!")
                    print("\n")
                    import time
                    time.sleep(1)
                    try_again = input("Would you like to play again? Type 'yes' or 'no'\n")
                    try_again = try_again.lower()
                    if try_again == "yes":
                              print("\n\n\n")
                              continue
                              
                    else: 
                              print("Thank you for playing!")
                              break