# Write a program to check if the list is sorted or not

l = [5,3,1,2,4]
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        continue
    else:
        print("Sorry, the list is not sorted")
        break
else:
    print("The list is sorted")