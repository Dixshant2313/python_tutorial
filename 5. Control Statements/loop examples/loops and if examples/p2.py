#WAP to accept gender from user and display the message based on their gender

gender = input("Enter your gender ").lower()
if (gender == "male"):
    print("Good Morning Sir") 
elif (gender == "female"):
    print("Good Morning Ma'am")
else:
    print(f"Good morning")