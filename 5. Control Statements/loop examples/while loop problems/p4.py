# create a random number guessing game using while loop
import random

num = random.randint(1,10)
print(num)
tries = 0
 
while True:
        guess = int(input("Guess the number between 1 and 10: "))
        if guess <= 10:
            if num == guess:
                tries += 1
                print(f"Great, you guessed it right in {tries} number of tries")  
                break
                
            elif num > guess:
                tries += 1
                print("Go a little higher")
            
            elif num < guess:
                tries += 1
                print("Go a little lower")
        else:
            print("Please enter a valid number")