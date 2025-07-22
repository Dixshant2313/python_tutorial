# Break statement is used to stop the loop immidiately once the condition is met

for num in range(1,10,1):
    if num == 5:
        break
        
    print(num)


'''
start = int(input("Enter the starting value: "))
stop = int(input("Enter the end value: "))
step = int(input("Enter the step up value: "))
mid_value = (start+stop)//2
for num in range(start, stop, step):
    if num == mid_value:
        break
    print(num)

'''