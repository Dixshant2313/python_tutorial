# Write a program to print the largest elemnet along with its index number
l = [5,7,9,2,1]
largest = l[0]
index = 0
for i in range(len(l)): 
    if largest < l[i]:   
        largest = l[i]
        index = i           

print(f"The largest number is {largest} at index value {index}")

'''
range will be (0,5) -> q k lenght tak chala hai 5 tak or 5 index exclude hoga
phle largest = 5
i = 5
condition false

largest = 5
i = 7
condition true
    largest = 7
    index = 1    
    
largest = 7
i = 9
condition true
    largest = 9
    index = 2
    
largest = 9
i = 2
condition false

largest = 9
i = 1
condition false

final output
9 2

start is by default 0
stop = len(l) i.e 5 -> isliye 0 se 4 chlega
'''