# parameters -> these acts as a placeholder for the values that are passed to the function when the fucntion is called
# arguments  -> these are the actual value that are passed when the function is called

def greet(a):                       # a --> parameter
    print(f"Hi {a}")

name = input("Enter your name ")    
greet(name)                         # name --> argument


''' 
In the above greet function we have given a parameter "a" which acts as a placeholder for the input variable "name". When the greet function is called using the variable "name" the placeholder variable or parameter value "a" is replaced by the input variable "name". 
'''

'''
There are 3 types of arguments
- positional 
- keywords 
- default

For more information, please go through the arguments folder
'''