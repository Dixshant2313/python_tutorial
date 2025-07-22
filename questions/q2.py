start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))
skip = int(input("Enter the number you want to skip: "))

if start > end:
    print("Invalid range, please try again!")
else:
    for i in range(start, end):
        if i == skip:
            continue
        print(i)
