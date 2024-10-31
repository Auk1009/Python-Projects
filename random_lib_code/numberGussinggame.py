import random
def numGussing(inputNumber, computerNumber):

    if inputNumber == computerNumber:
        print("Good you guessed it correctly")
        return True
    else:
        print("Incorrect try again")
        return False
    

score = 0
while(True):
    inputNumber = int(input('think of a number between 1 to 10: '))
    generatedNumber = numgenerator = random.randint(1, 5)
    print("Generated Number:", generatedNumber)
    print("Input Number:", inputNumber)
    if numGussing(inputNumber,generatedNumber) :
        score = score + 1
    print("Your score is:", score)


