"""
->  A lambda function is an anonymous, inline function defined using the lambda keyword.
->  It's pften used for short, simple functions that are used only once or temprarily.
->  You can have multiple arguments but there will be only one expression.

Traditional way to create function
    def addition(a,b):
        return a+b
        
print(addition(4,5))

Syntax of lamba function:- lambda arguments: actions to be performed
"""

#lambda function to create the same
addition = lambda a,b : a + b
print(addition(4,5))

# another example to check even or odd using if-else with lambda function
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(5))