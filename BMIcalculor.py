# A Calculator for BMI
Name=input("What is your name? ")
print("Hello " + Name)
Weight=input("What is your weight in Kilograms? ")
convert_height = input("Do you want to convert your height into meters? (Y/N): ")
if convert_height.lower() in ["y", "yes"]:
    tf_height = float(input("What is your height in feet? "))
    Height = tf_height * 0.3048
    print(f"Your height in meters is {Height}")
else:
    Height = float(input("What is your height in Meters? "))
BMI=float(Weight)/float(Height)**2
print(f"Your BMI is {BMI}")