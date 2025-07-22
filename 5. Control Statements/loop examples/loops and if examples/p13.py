# Write a program to print all the factorials of a number

num = int(input("Enter your number: "))
for i in range(1, num+1):
    if(num%i==0):
        print(i)