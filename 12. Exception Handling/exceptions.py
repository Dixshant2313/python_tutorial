# Exceptions are unexpected events or errors that occurs during the execution of a program, which disrupts the normal flow of program.

# print("Start")
# print(10/0)     # Raise Zero DIvision Error     
# print("End")    # This line will never be executed

# The above mentioned is a zero division error and can be counted as exception becuase of which the next line of code cannot be executed

"""
Keywrods in Exception Handling
try     ->  wrap the block of code that might cause an exception
except  ->  Handle the exception if it occurs
else    ->  run code only if no execution occurs
finally ->  run the code no matter what, there's an exception or nou
raise   ->  manually throws and exceptio
"""

a = int(input("Enter the number: "))

try:
    print(10/a)
    
except Exception as err:
    print(f"Encountered an error: {err}")
    
else:
    print("There is no exception")
    
finally:
    print("Division complete")
    
# raise 
age = int(input("Enter your age: "))

if age<10 or age>18:
    raise ValueError("Does not meet the age criteria")
else:
    print("Welcome to the club")
    
print("The game starts soon!")