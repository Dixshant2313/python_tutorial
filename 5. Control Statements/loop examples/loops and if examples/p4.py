# Write a program to take name and age as input from user and check if user is eligible fot voting or not

name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"Hi {name}, you're eligible for voting")
else:
    print(f"Sorry {name}, you're not eligible for voting")