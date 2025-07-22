# Write a program to take input from the user and perform desired arithmetic operation as per the input
a = 10
b = 2
operation = input("Enter the arithemetic operation ")
if (operation == "+"):
    print(f"Sum = {a+b}")
elif (operation == "-"):
    print(f"Difference = {a-b}")
elif (operation == "*"):
    print(f"Product = {a*b}")
elif (operation == "/"):
    print(f"Quotient = {a/b}")
else:
    print("Invalid Input!")
