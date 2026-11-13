import random
import sys
print("-----WELCOME!-----")
print("This is a number guessing game! Here are some instructions to help you play")
print("1. The system will pick a random number between 1 to 100 (both inclusive) \n2. You have to enter a number to try and guess the random number.\n3. You will be provided comments to indicate how close you are to the number. \n4. You only have 7 tries.")
guessNumber = random.randint(1,100)
guessTries = 0
while(guessTries < 7):
    try : 
        userNumber = int(input("Enter your guess : "))
    except : 
        print("Enter valid guess! (A number between 1 and 100)")
        sys.exit(1)
    if (guessNumber > userNumber):
        print("Too low! Guess higher!")
    elif (guessNumber < userNumber):
        print("Too high! Guess lower!")
    else:
        print("You got it right!")
        sys.exit(0)
    guessTries = guessTries + 1
print("Better luck next time!")
print("The number was : ", guessNumber)
sys.exit(0)