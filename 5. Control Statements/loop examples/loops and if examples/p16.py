# Write a program to reverse a string using for loop

text = input("Enter the text to reverse: ").lower()
rev = ""
for i in range(len(text)-1, -1 , -1):
    rev+= text[i]

print(rev)

    
