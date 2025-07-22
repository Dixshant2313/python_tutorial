# Write a program to take input from user for the marks and check if student is passed, failed or passed with grace.

Maths = int(input("Enter the marks obtained in maths "))
English = int(input("Enter the marks obtained in English "))
History = int(input("Enter the marks obtained in history "))
if (Maths>=33 and English>=33 and History>=33 ):
    print("Congo, You are passed ")
elif (Maths>=33 and English>=33 or History>=33 and Maths>=33 or English>=33 and History>=33 ):
#elif ((Maths and English >=33 and History<33) or (Maths<33 and History and English >=33) or (Maths and History >=33 and English<33)):
     print("You are passed with grace ")
else:
     print("Alas! You are Failed")

