# It will Generate a Custum Password
import random
# Define the characters that can be used in the password
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Generate the password
# Ask the user for the number of Number in the password
num_number = int(input("Enter the number of numbers in the password: "))
# Ask the user for the number of chracters in the password
num_characters = int(input("Enter the number of characters in the password: "))
# Ask the user for the number of symbols in the password
num_symbols = int(input("Enter the number of symbols in the password: "))
# Generate the password
password = []
for num in range(num_number):
  password+=random.choice(numbers)
for char in range(num_characters):
  password += random.choice(characters)
for sym in range(num_symbols):
  password += random.choice(symbols)

# Shuffle the password
random.shuffle(password)
# Convert the password to a string
password = ''.join(password)
print(password)