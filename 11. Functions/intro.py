'''
Function is a block of reusable code that perform a specific task and can be executed by calling the function name. This helps in avoiding repitition and makes programs modular and readable

Advantages:
1. Functions are reusable 
2. reduces complexity
3. scoping


Disadvantages:-
1. If not designed properly, it will consume more memory and time, making the program sluggish.
2. If the code is not maintained properly, program becomes complex.

Basic syntax:-
def function_name(parameters):      ----> function definition
    task to be performed
    .
    .
    .
    
function_name(values)               ----> function calling     
'''

# Basic function example
def greet():
    print("Hi!")

greet()


# function to perform sum of two numbers
def add(a,b):
    print(f"Sum = {a+b}")
    
num_1 = int(input("Enter the value of a = "))
num_2 = int(input("Enter the value of b = "))

sum = add(num_1,num_2)