# Write a program to check if the given number is a palindrome or not

num = int(input("Enter the number to check: "))
rev_num = 0
num_copy = num
while (num > 0):
    rev_num = num%10 + rev_num*10
    num //= 10
    
if (rev_num == num_copy):
    print("Palindrome")
else:
    print("Not a Palindrome")