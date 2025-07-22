# Write a python program to sum all the values in a dictionary
d = {1:10,2:20,3:30,4:40}
sum = 0
for i in d:
    sum += d[i]
    
print(f"Sum of all values = {sum}")