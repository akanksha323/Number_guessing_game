import random

range1 = 0
range2 = 0
userPlay = True
userScore = 0
maxTries = 0

def instructions():
    print()
    print()
    print("---------------WELCOME!---------------")
    print("This is a number guessing game! Here are some instructions to help you play : ")
    print("1. The system will pick a random number between a range as per the difficulty level. \n2. You have to enter a number to try and guess the random number.\n3. You will be provided comments to indicate how close you are to the number. \n4. You have limited number of attempts.\n5. Press Y to continue playing and any other key to discontinue the game.")
    print()
   

def difficultyEasy():
    global maxTries
    maxTries = 8
    global range1 
    range1 = 1
    global range2 
    range2 = 50
    print("The scoring system is as follows : \n-> Right on 1st try : 80 points\n-> Right on 2nd try : 70 points\n-> Right on 3rd try : 60 points \n-> Right on 4th try : 50 points\n-> Right on 5th try : 40 points \n-> Right on 6th try : 30 points \n-> Right on 7th try : 20 points\n-> Right on 8th try : 10 points. ")
    print()
    

def difficultyMedium():
    global maxTries 
    maxTries = 7
    global range1 
    range1 = 1
    global range2
    range2 = 100
    print("The scoring system is as follows : \n-> Right on 1st try : 70 points\n-> Right on 2nd try : 60 points\n-> Right on 3rd try : 50 points \n-> Right on 4th try : 40 points\n-> Right on 5th try : 30 points \n-> Right on 6th try : 20 points \n-> Right on 7th try : 10 points ")
    print()

def difficultyHard():
    global maxTries 
    maxTries = 8
    global range1 
    range1 = 1
    global range2 
    range2 = 200
    print("The scoring system is as follows : \n-> Right on 1st try : 80 points\n-> Right on 2nd try : 70 points\n-> Right on 3rd try : 60 points \n-> Right on 4th try : 50 points\n-> Right on 5th try : 40 points \n-> Right on 6th try : 30 points \n-> Right on 7th try : 20 points\n-> Right on 8th try : 10 points. ")
    print()

instructions()

while(userPlay):
    guessTries = 0
    gameResult = False

    try : 
        difficultyChosen = int(input("Enter : \n1 for Easy difficulty\n2 for Medium difficulty\n3 for Hard difficulty\nYour Choice: "))
        print()

        if difficultyChosen == 1:
            difficultyEasy()
        elif difficultyChosen == 2:
            difficultyMedium()
        elif difficultyChosen == 3:
            difficultyHard()
        else :
            print("Enter valid input (1/2/3)")
            continue

    except ValueError : 
        print("Enter valid input (1/2/3)")
        continue

    print(f"The range is between {range1} and {range2}\nMaximum number of attempts allowed are {maxTries}")
    guessNumber = random.randint(range1,range2)
    print()

    while(guessTries < maxTries):
        try : 
            userNumber = int(input("Enter your guess : "))
            if userNumber < range1 or userNumber > range2:
                print(f"Enter valid guess! (A number between {range1} and {range2})")
                continue

        except ValueError: 
            print(f"Enter valid guess! (A number between {range1} and {range2})")
            continue
        guessTries = guessTries + 1
        if (guessNumber > userNumber):
            print("Too low! Guess higher!")
        elif (guessNumber < userNumber):
            print("Too high! Guess lower!")
        else:
            print("You got it right!")
            gameResult = True
            break
        print("You have ",maxTries-guessTries," guesses left.")
        print()
    if (not gameResult):
        print("Better luck next time!")
        print("The number was : ", guessNumber)

    else:
        userScore = userScore + 10 * (maxTries + 1 - guessTries)
    print("Your total score is : ", userScore)

    
    userChoice = input("Do you wish to continue the game? (PRESS Y TO CONTINUE) : ")
    if(userChoice.lower() != "y"):
        userPlay = False

print("----------THANK YOU FOR PLAYING!----------")
