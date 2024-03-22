import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
comp = random.choice([rock, paper, scissors])
print("Welcome to Rock, Paper, Scissors!")
print("Lets play!")
print("Choose your weapon! 1. Rock, 2. Paper, 3. Scissors")
player = int(input(""))
if player == 1:
  print(rock)
  print("You chose Rock!")
  if comp == rock:
    print(rock)
    print("Computer chose Rock!")
    print("It's a draw!")
  elif comp == paper:
    print(paper)
    print("Computer chose Paper!")
    print("You lose!")
  else:
    print(scissors)
    print("Computer chose Scissors!")
    print("You win!")
elif player == 2:
  print(paper)
  print("You chose Paper!")
  if comp == rock:
    print(rock)
    print("Computer chose Rock!")
    print("You win!")
  elif comp == paper:
    print(paper)
    print("Computer chose Paper!")
    print("It's a draw!")
  else:
    print(scissors)
    print("Computer chose Scissors!")
    print("You lose!")
elif player == 3:
  print(scissors)
  print("You chose Scissors!")
  if comp == rock:
    print(rock)
    print("Computer chose Rock!")
    print("You lose!")
  elif comp == paper:
    print(paper)
    print("Computer chose Paper!")
    print("You win!")
  else:
    print(scissors)
    print("Computer chose Scissors!")
    print("It's a draw!")
else:
  print("Invalid input, try again!")
