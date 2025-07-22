'''

Write a program to input the range from user and when the condition is met skip the value and if the start value > end value print (Invalid input!)

'''

start_value = int(input("Enter the starting value: "))
stop_value = int(input("Enter the ending value: "))
step_up_value = int(input("Enter the step up value: "))
skip_value = int(input("Enter the skip value: "))
if (start_value > stop_value):
    print("Invalid input!")
else:
    for a in range(start_value, stop_value, step_up_value):
        if a == skip_value:
            continue
        print(a)


    