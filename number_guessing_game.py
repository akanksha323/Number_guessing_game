import random

def instructions():
    print("-----WELCOME!-----")
    print("This is a number guessing game! Here are some instructions to help you play : ")
    print("1. The system will pick a random number between 1 to 100 (both inclusive) \n2. You have to enter a number to try and guess the random number.\n3. You will be provided comments to indicate how close you are to the number. \n4. You only have 7 tries.\n5.Press Y to continue playing and any other key to discontinue the game.")
    print()
    print("The scoring system is as follows : \n-> Right on 1st try : 70 points\n-> Right on 2nd try : 60 points\n-> Right on 3rd try : 50 points \n-> Right on 4th try : 40 points\n-> Right on 5th try : 30 points \n-> Right on 6th try : 20 points \n-> Right on 7th try : 10 points ")
    print()

instructions()

userPlay = True
userScore = 0
maxTries = 7
while(userPlay):
    guessTries = 0
    guessNumber = random.randint(1,100)
    while(guessTries < maxTries):
        try : 
            userNumber = int(input("Enter your guess : "))
            if userNumber < 1 or userNumber > 100:
                print("Enter valid guess! (A number between 1 and 100)")
                continue

        except ValueError: 
            print("Enter valid guess! (A number between 1 and 100)")
            continue

        if (guessNumber > userNumber):
            print("Too low! Guess higher!")
        elif (guessNumber < userNumber):
            print("Too high! Guess lower!")
        else:
            print("You got it right!")
            break
        guessTries = guessTries + 1
        print("You have ",maxTries-guessTries," guesses left.")
        print()
    if (guessTries == maxTries):
        print("Better luck next time!")
        print("The number was : ", guessNumber)
    userScore = userScore + 10 * (maxTries + 1 - guessTries)
    print("Your total score is : ", userScore)

    
    userChoice = input("Do you wish to continue the game? (PRESS Y TO CONTINUE) : ")
    if(userChoice != "y" and userChoice != "Y"):
        userPlay = False
