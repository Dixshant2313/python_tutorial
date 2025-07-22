# Write a program to print all the positive and negative numbers in a list

l = [1,2,-4,-5.5,7,8,-3]
pos_list = []
neg_list = []

for i in l:
    if i < 0.0:
        neg_list.append(i)
    else:
        pos_list.append(i)
        
print(f"Negative numbers in list = {neg_list}")
print(f"Positive numbers in list = {pos_list}")

