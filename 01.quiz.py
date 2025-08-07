print("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    print("Okay, maybe next time!")
    quit()
    
print("Great! Let's start the quiz.")

score = 0
#First question
answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
#Second question

answer = input("What is 2 + 2? ")
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

#Third question

answer = input("What is the largest planet in our solar system? ")
if answer.lower() == "jupiter":
    print("correct!")
    score += 1
else:
    print("InCorrect!")
    
# print("you scored " + str(score) + " questions correctly.")
percentage = round((score / 3) * 100,2)
print(f"you scored {percentage:.2f}% questions correctly.")
print("Thanks for playing the Quiz Game!")
    
    