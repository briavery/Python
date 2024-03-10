import random

randomNum = random.randint(1, 100)

def main():
    userGuess = -1
    while userGuess != randomNum:
        try:
            userGuess = int(input("Guess a number: "))
            numDiff = abs(userGuess - randomNum)
            if numDiff == 0:
                print("You guessed the number!")
            elif numDiff <= 5:
                print("Very Hot")
            elif numDiff <= 15:
                print("Hot")
            elif numDiff <= 25:
                print("Cool")
            else:
                print("Cold")

        except ValueError:
            print("Ran into a Value Error")

main()           