# Write a program to extract the digits from a number

number = int(input("Enter the number: "))
while (number > 0):
    print(number % 10)
    number //= 10

"""
number = 568
True
8
56

number = 56
True
6
5

number = 5
True
5
0.5 == 0
"""