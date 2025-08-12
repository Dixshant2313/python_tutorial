# Ternary operations: converts the if else condition into a single line of code
a = 12
print("Even") if a%2==0 else print("Odd")

# List comprehension
lst = [x for x in range(1,21) if x % 2==0]
print(lst)

# Dictionary comprehension
d = {i:i*i for i in range(1,11) if i % 2 == 0}
print(d)

# Set comprehension
unique_even_squares = {x*x for x in range(11) if x % 2 ==0}
print(unique_even_squares)