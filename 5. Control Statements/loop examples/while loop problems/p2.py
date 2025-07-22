# Write a program to reverse a number using while loop

num = int(input("Enter the number: "))
rev_num = 0
while (num > 0):
    rev_num = num % 10 + rev_num*10
    num //= 10
print(rev_num)

"""
num = 568
rev_num = 8 + 0 = 8
num = 56

num = 56
rev_num = 6 + 80 = 86
num = 5

num = 5
rev_num = 5 + 860 = 865
num = 0

condition False -> loop exit
rev_num = 865
"""



"""
name = "Shreya"
rev_name = ""
for i in range(len(name)):
    rev_name += name[i]
    
ayerhS
"""