# Write a program to check for perfect number
"""
a number is a perfect number when the sum of factors of that number (excluding the number) is equal to the number itself
eg. 6 -> 1+2+3 = 6 
"""

num = int(input("Enter the number to check: "))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+= i
        
if(sum==num):
    print("Number is a Perfect Number")
else:
    print("Number is not a Perfect Number!")
        


