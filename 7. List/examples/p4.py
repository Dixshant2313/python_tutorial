# Write a program to print the second largest element in the list

l = [5,12,568,79,81]
largest = l[0]
sec_largest = l[0]

for i in range(len(l)):
    if l[i] > largest:
        sec_largest = largest
        largest = l[i]
    elif l[i] > sec_largest:
        sec_largest = l[i]

print(f"The largest number is {largest} and the second largest is {sec_largest}")

#easy peasy
l2 = [79,87,-5,24,57]
l2.sort()
print(f"The largest number is {l2[-1]} and the second largest number is {l2[-2]}")