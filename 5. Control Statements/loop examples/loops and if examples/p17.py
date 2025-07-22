# Write a program to check a string is palindrome or not using for loop

text = input("Enter the text: ").lower()
reversed_text = ""
for i in range(len(text)-1, -1, -1):
    reversed_text+= text[i]
 
if(reversed_text==text):
     print("It is a Palindromic String")
else:
     print("Not a Palindromic String")
     

