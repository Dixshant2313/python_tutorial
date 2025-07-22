# Write a program to check if the number is prime or not

num = int(input("Enter the number to check: "))
fact = 0
for i in range(1, num+1):
    if(num%i==0):
        fact += 1
        

if fact == 2:
    print("It is a prime number")
else:
    print("It is not a prime number") 
       

"""        
num = int(input("Enter the number to check: "))
for i in range(2, num):
    if(num%i==0):
        print("It is a not a prime number")
        break
else:
    print("It is a prime number")
"""
    
