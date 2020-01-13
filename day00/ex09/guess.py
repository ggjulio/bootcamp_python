import sys
import random

min = 1
max = 99

guest_n = random.randint(min,max)

print(guest_n, end='\n\n')

print ("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")

i = 0
while 1:
    i += 1
    try:
        n = input(f"What's your guess between {min} and {max} ?\n>> ")
        if n == "exit":
            sys.exit("Goodbye!")
        n = int(n);
    except ValueError:
        print ("That's not a number.")
        continue
    if n < guest_n:
        print ("Too low!")
    elif n > guest_n:
        print ("Too high!")
    else:
        break
if guest_n == 42:
    print("The answer to the ultimate question of life, the universe and everything is 42.")
else:
    print("Congratulations, you've got it!")
    
if i == 1:
    print("You got it on your first try!")
else:
    print(f"You won in {i} attempts!")

