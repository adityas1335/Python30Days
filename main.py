# HOME

user_choice = input(
    " 1 for BMIcalculor\n 2 for YTNameGenerator \n 3 for R_P_C_Game \n 4 Finding Treasure\n 5 PasswordGenerator \nWhich module do you want to work with?\n Enter: "
)

if user_choice == '1':
  import BMIcalculor
elif user_choice == '2':
  import YTNameGenerator
elif user_choice == '3':
  import R_P_C_Game
elif user_choice == '4':
  import FindTreasure
elif user_choice == '5':
  import PasswordGenerator
else:
  print("Invalid choice. Please enter 1 or 2 or 3 or 4 or 5.")

  # run the program again user want
user_choice = input("Do you want to run again? Enter 'Y' to continue: ")
if user_choice.lower() == 'y':
  import main
else:
  print("Thank you for using. Goodbye!")
