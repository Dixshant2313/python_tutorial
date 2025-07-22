# Write a program to print the factorial of a number

num = int(input("Enter the number "))
fac = 1
for i in range(1, num+1):
    fac= fac*i
    
print(f"Factorial of the {num} is {fac}")
    