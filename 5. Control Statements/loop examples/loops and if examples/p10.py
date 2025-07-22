# Write a program to print sum of n natural numbers

"""
n = int(input("Enter the number: "))
for i in range(1,n,1):
    n+=i
    print(i,n)
"""
    
"""
n = 8
i = 1
9

n = 9
i = 2
n = 11

n = 11
i = 3
n = 14

n = 14
i = 4
n = 18

n = 18
i = 5
n = 23

n = 23
i = 6
n = 29

n = 29
i = 7
n = 36
"""

num = int(input("Enter the number "))
sum = 0
for i in range(1,num+1,1):
    sum += i

print(f"Sum of first {num} natural numbers = {sum}")