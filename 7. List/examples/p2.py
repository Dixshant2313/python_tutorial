# Write a program to find the mean of all elements in a list

l = [1,5.5,7,9,4,2]
sum = 0

for i in l:
    sum += i
    
mean = sum/len(l)
print(f"Mean of elements in the list = {mean}")

