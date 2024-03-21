# HOME

user_choice = input("Which module do you want to work with? Enter 1 for BMIcalculor, 2 for YTNameGenerator: ")

if user_choice == '1':
    import BMIcalculor
elif user_choice == '2':
    import YTNameGenerator
else:
    print("Invalid choice. Please enter 1 or 2.")

