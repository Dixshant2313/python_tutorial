"""
A generator is a function that yields values one at a time using the yield keyword instead of return. It allows you to iterate through a potentially large dataset without storing it all in memory.

- Memory efficient
- Lazy evaluation (produces items only when needed)

Syntax :->  def generator_func():
                yield value
"""

def count_down(num):
    while num > 0:
        yield num       #yields value one at a time
        num -= 1
        
#using generator
for number in count_down(5):
    print(number)
    
   