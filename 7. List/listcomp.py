"""

Traditional method to create a list of squares till 10

squares = []
for i in range(1,11):
    squares.append(i ** 2)
print(squares)
"""

squaures = [i ** 2 for i in range(1,11) if i % 2 == 0]
print(squaures)
