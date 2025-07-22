# Write a python program to merge two python dictionaries

d1={"name":"Amit","age":25,"gender":"M"}
d2={"email":"amit.kumar@yahoo.com","phone":9837451991}

for i in d2:
    d1[i] = d2[i]
    
print(d1)