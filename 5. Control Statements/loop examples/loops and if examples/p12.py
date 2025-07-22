# Write a program to print the sum of all odd and even numbers in a range separately

num = int(input("Enter the number "))
sum1=0
sum2=0 
for i in range(1, num):
    if(i%2==0):
        sum1+= i
    else:
        sum2+= i
        
print(f"Sum of Even numbers ={sum1}")
print(f"Sum of Odd numbers ={sum2}")
        