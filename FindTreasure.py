#Finding Treasure Game

import random 
print("Welcome to 'Finding Treasure'!")
user_input = input("Press 1 to start the game: ")
if user_input == "1":
#Game Started
  print("You have Entered a Cave and found two cannal, one is in right and one is in left")
  user_input = input("right or left: ")
  if user_input.lower() == "left":
    print("You are Out of the Cave and Completed Level 1 Sucessfully")
    user_input = input("Choose a path - Press 1 for the first path, Press 2 for the second path, Press 3 for the third path, Press 4 for the fourth path: ")
    if user_input == "4":
        print("You have completed Level 2 Sucessfully")
        print("You have reached 8 palaces, one of them has a treasure while others are traps. Choose wisely!")
        user_input = input("Enter the palace number from 1 to 8: ")
        if user_input == "5":
            print("You have completed Level 3 Sucessfully")
            print("Inside the palace, you found 16 boxes. Only one of them contains the real treasure. Rest of the boxes are booby traps. Choose wisely!")
            user_input = input("Enter the box number from 1 to 16: ")
            if user_input == "8":
                print("Congratulations! You have found the real treasure!")
            else:
                print("Oh no! You opened a trap box. Game Over!")
        else:
            print("Oh no! You chose the wrong palace. It's a trap. Game Over!")
    else:
        print("You have been attacked by a monster. Game Over!")
  else:
    print("You have fallen into a pit and died. Game Over!")
else:
  print("Bye Bye..... Please try again.")