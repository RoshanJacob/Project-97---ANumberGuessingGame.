import random

myChances = [0, 0, 0, 0, 0]
randomNumber = random.randint(1, 9)

print("Number Guessing Game!")

while(len(myChances) > 0 ):
    myInput = int(input("Type a number between 1 and 9! :"))
    if(myInput < randomNumber):
        print("Wrong Guess! Try again.")
        print("Try guessing numbers above" + " " + str(randomNumber - random.randint(1, 3)))
        myChances.pop()
    elif(myInput > randomNumber):
        print("Wrong Guess! Try again.")
        print("Try guessing numbers below" + " " + str(randomNumber + random.randint(1, 3)))
        myChances.pop()
    elif(myInput == randomNumber):
        print("Congratulations! You guessed the correct number! You have mastered this game!")
        break

else:
    print("Oh no! You have run out of chances! Try again")