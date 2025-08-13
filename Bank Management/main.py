import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read()) 
        else:
            print("No such file exists! ")
    except Exception as err:
        print(f"An error occured as {err}")    
    
    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    @staticmethod
    def __accountgenerate():
        alpha = random.choices(string.ascii_letters,k=4)
        num = random.choices(string.digits,k=3)
        splchar = random.choices("@&$#",k=1)
        id = alpha + num + splchar
        random.shuffle(id)
        return "".join(id)
    
    def CreateAccount(self):
        info = {
            "name": input("Please enter your name: "),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Please enter the PIN: ")),
            "A/C No.": Bank.__accountgenerate(),
            "Balance": 0
        }
        if info["age"] < 18 or len(str(info["pin"])) != 4 or "@" not in info["email"]:
            print("Sorry you cannot create your account")
        else:
            for i in info:
                print(f"{i} : {info[i]}")
            print("Account created successfully")
            print("Please note down your A/C number")
            
            Bank.data.append(info)
            
            Bank.__update()
            
    def DepositMoney(self):
        accNumber = input("Please enter the account number: ")
        pin = int(input("Please enter the account PIN: "))
        
        userdata = [i for i in Bank.data if i["A/C No."] == accNumber and i["pin"] == pin]
        if userdata == False:
            print("Sorry, account does not exist!")
        else:
            amount = int(input("Enter the amount to deposit (Max: 10000)- "))
            if amount > 10000 or amount < 0:
                print("Sorry, deposit limit exceed!, please enter a smaller amount")
            else:
                userdata[0]["Balance"]+= amount
                Bank.__update()
                print("Amount deposited successfully")
                print(f"Updated balance = ₹{userdata[0]["Balance"]}")
    
    def WithdrawMoney(self):
        accNumber = input("Please enter the account number: ")
        pin = int(input("Please enter the account PIN: "))
        
        userdata = [i for i in Bank.data if i["A/C No."] == accNumber and i["pin"] == pin]
        if userdata == False:
            print("Sorry, account does not exist!")
        else:
            amount = int(input("Enter the amount to withdraw- "))
            if amount < 0:
                print("Entered an invalid amount!")
            elif amount > userdata[0]["Balance"]:
                print("Insufficient funds")
            else:
                userdata[0]["Balance"] -= amount
                print(f"Withdrawl successful, Updated balance = ₹{userdata[0]["Balance"]}")
    
    def ShowAccount(self):
        accNumber = input("Please enter the account number: ")
        pin = int(input("Please enter the account PIN: "))
        
        userdata = [i for i in Bank.data if i["A/C No."] == accNumber and i["pin"] == pin]
        if userdata == False:
            print("Sorry, account does not exist!")
        else:
            print("\n\nACCOUNT DETAILS: ")
            for i in userdata[0]:
                print(f"{i}: {userdata[0][i]}")
        
    def UpdateAccount(self):
        accNumber = input("Please enter the account number: ")
        pin = int(input("Please enter the account PIN: "))
        
        userdata = [i for i in Bank.data if i["A/C No."] == accNumber and i["pin"] == pin]
        if userdata == False:
            print("Sorry, account does not exist!")
            
        else:
            print("You cannot change the age, A/C number")
            print("Fill the details to change or leave it empty if no change is required")
            newdata = {
                "name": input("Please tell new name or press enter to skip: "),
                "email": input("Please tell new email or press enter to skip: "),
                "pin": input("Enter new PIN or press enter to skip: ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]
                
            newdata["age"] = userdata[0]["age"]
            newdata["A/C No."] = userdata[0]["A/C No."]
            newdata["Balance"] = userdata[0]["Balance"]

            if type(newdata["pin"]) == str:
                newdata["pin"] = int(newdata["pin"])
                
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            print("\nAccount details updated successfully")
            for j in userdata[0]:
                print(f"{j}: {userdata[0][j]}")
            
            Bank.__update()
            
    def CloseAccount(self):
        accNumber = input("Please enter your account number: ")
        pin = int(input("Please enter your account PIN: "))
        
        userdata = [i for i in Bank.data if i['A/C No.'] == accNumber and i['pin'] == pin]
        if userdata == False:
            print("Sorry, no such user exists!")
        else:
            check = input("Press Y or N for confirmation: ").lower()
            if check == 'n':
                print("Account deletion cancelled as per the request")
            elif check == 'y':
                index  = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully ")
                Bank.__update()
            else:
                print("Invalid input!")

user = Bank()

print("Press 1 for creating an account: ")
print("Press 2 for depositing the money: ")
print("Press 3 for withdrawing the money")
print("Press 4 for bank A/C details: ")
print("Press 5 for updating A/C details: ")
print("Press 6 for closing the A/C: ")

check = int(input("Please enter your response: "))

match check:
    case 1:
        user.CreateAccount()
    case 2:
        user.DepositMoney()
    case 3:
        user.WithdrawMoney()
    case 4:
        user.ShowAccount()
    case 5:
        user.UpdateAccount()
    case 6:
        user.CloseAccount()
    case _:
        print("Invalid choice!") 
