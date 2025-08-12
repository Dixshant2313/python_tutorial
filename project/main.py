from pathlib import Path
import os

def readFileandFolder():
    path = Path('')
    items = list(path.rglob('*'))
    print("Files present in the current directory:")
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readFileandFolder()
        name = input("Please tell the file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data = input("What do you want to write in this file :- ")
                fs.write(data)
        
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("File already exists")
    
    except Exception as err:
        print(f"An error occured: {err}")
        
def readfile():
    try:
        readFileandFolder()
        name = input("Which file do you want to read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
                
            print("FILE READ SUCCESSFULLY")
        else:
            print("FILE DOES NOT EXIST")
    except Exception as err:
        print(f"An error occured: {err}")
        
def updatefile():
    try:
        readFileandFolder()
        name = input("Enter the name of the file you want to update:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 to update the file name:- ")
            print("Press 2 to update the file data:- ")
            print("Press 3 to append the data in your file:- ")
            
            res = int(input("Enter your response:- "))
            
            if res == 1:
                name2 = input("Enter new file name:- ")
                p2 = Path(name2)
                p.rename(p2)
                
            if res == 2:
                with open(p,'w') as fs:
                    data = input("Enter the text to overwrite the data in your file")
                    fs.write(data)
                    
            if res == 3:
                with open(p,'a') as fs:
                    data = input("Enter the text to append in your file")
                    fs.write(" "+data)
            
            print("FILE UPDATED SUCCESSFULLY")  
        else:
            print("File not found!")
    except Exception as err:
        print(f"An error occured: {err}")  
        
def deletefile():
    try:
        
        readFileandFolder()
        name = input("Enter the file name you want to delete:- ")
        p =Path(name)
        if p.exists() and p.is_file():
            os.remove(p)  
            
            print("FILE DELETED SUCCESSFULLY")
        else:
            print("No such file exists")
            
    except Exception as err:
        print(f"An error occured: {err}")
        

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

try:
    check = int(input("Please tell your response :- "))

    match check:
        case 1:
            createfile()
        case 2:
            readfile()
        case 3:
            updatefile()
        case 4:
            deletefile()        
except ValueError:
    print("❌ Invalid input. Please enter a numeric value 1-4: ")
    
    
# using match case for clean code
'''
from pathlib import Path
import os

def readFileandFolder():
    path = Path('.')
    items = list(path.rglob('*'))
    print("\nFiles present in the current directory:\n")
    for i, item in enumerate(items):
        if item.is_file():
            print(f"{i+1}: {item.name}")

def createfile():
    try:
        readFileandFolder()
        name = input("\nEnter the name of the file to create: ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Enter the content to write in this file: ")
                fs.write(data)
            print("✅ FILE CREATED SUCCESSFULLY")
        else:
            print("⚠️ File already exists.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

def readfile():
    try:
        readFileandFolder()
        name = input("\nEnter the name of the file to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print("\nFile Content:\n")
                print(data)
            print("\n✅ FILE READ SUCCESSFULLY")
        else:
            print("⚠️ File does not exist.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

def updatefile():
    try:
        readFileandFolder()
        name = input("\nEnter the name of the file to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("\nUpdate Options:")
            print("1. Rename the file")
            print("2. Overwrite the file content")
            print("3. Append content to the file")
            res = int(input("Choose an option (1/2/3): "))

            match res:
                case 1:
                    name2 = input("Enter the new file name: ")
                    p.rename(Path(name2))
                    print("✅ File renamed successfully.")
                case 2:
                    with open(p, 'w') as fs:
                        data = input("Enter new content to overwrite the file: ")
                        fs.write(data)
                    print("✅ File content overwritten.")
                case 3:
                    with open(p, 'a') as fs:
                        data = input("Enter content to append to the file: ")
                        fs.write(" " + data)
                    print("✅ Content appended to the file.")
                case _:
                    print("⚠️ Invalid update option.")
        else:
            print("⚠️ File does not exist.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

def deletefile():
    try:
        readFileandFolder()
        name = input("\nEnter the name of the file to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("✅ FILE DELETED SUCCESSFULLY")
        else:
            print("⚠️ File does not exist.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

# ---------- MAIN MENU ----------
print("\n📁 File Handling Menu")
print("1. Create a file")
print("2. Read a file")
print("3. Update a file")
print("4. Delete a file")

try:
    check = int(input("\nPlease select an option (1–4): "))

    match check:
        case 1:
            createfile()
        case 2:
            readfile()
        case 3:
            updatefile()
        case 4:
            deletefile()
        case _:
            print("⚠️ Invalid option. Please enter a number from 1 to 4.")

except ValueError:
    print("❌ Invalid input. Please enter a numeric value.")

'''
