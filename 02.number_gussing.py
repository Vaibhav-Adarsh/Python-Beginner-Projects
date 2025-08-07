import random

top_of_range = input("Enter the top of the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0.")
        quit()
else:
    print("Please enter a valid number.")
    quit()
    
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_gusse = input("Make a guess: ")
    if user_gusse.isdigit():
        user_gusse = int(user_gusse)
    else:
        print("Please enter a valid number.")
        continue
    
    if user_gusse == random_number:
        print("You got it!")
        break
    elif user_gusse > random_number:
        print("You are above the number.")
    else:
        print("You are below the number.")
print(f"You guessed the number in {guesses} tries.")
print("Thanks for playing the Number Guessing Game!")