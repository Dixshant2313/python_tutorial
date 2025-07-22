# Write a program to combine two dictionaries by adding values for common keys

d1 = {1:5,2:10,3:9,4:16}
d2 = {3:17,4:7,5:2,6:4}

combined_dict = d1.copy()

for key in d2:
    if key in combined_dict:
        combined_dict[key] += d2[key]
    else:
        combined_dict[key] = d2[key]

print(combined_dict)