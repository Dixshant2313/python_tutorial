# Write a program to check if the entered value is a palindrome or not
#-> For example: "Naman, 121 is a palindrome"

#Using slicing method

text = input("Enter the text to check: ").lower()
reversed_text = text[::-1]
if reversed_text == text:
    print("Palindrome")
else:
    print("Not Palindrome")
