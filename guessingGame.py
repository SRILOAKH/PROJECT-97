import random
print("Number Guessing Game")
NUMBER=random.randint(1,9)
chances=0
print("Guess a number(between 1 and 9)")
while chances<5:
    GUESS=int(input("Enter your guess"))
    if(GUESS==NUMBER):
        print("Congratulation YOU WON")
        break
    elif(GUESS<NUMBER):
        print("Your guess was too low:Guess a number higher than",GUESS)
    else:
        print("Your guess was too high:Guess a number lower than",GUESS)
    chances+=1
    if not chances<5:
        print("You Lose,The number is ",NUMBER)