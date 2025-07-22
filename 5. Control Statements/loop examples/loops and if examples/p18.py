# Write a program to count the digits, characters and special characters in a string

text = input("Enter your text: ")
char = 0
dig = 0
spchr = 0

for i in text:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        spchr += 1


print(f"The entered string has {char} alphabets, {dig} digits and {spchr} special characters")