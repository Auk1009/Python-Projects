import random

def logic(inputNumber, generatedNumber):
    if inputNumber == generatedNumber:
        print('Correct')
        return True
    else:
        print('Incorrect')
        return False
score = 0
while(True):
    inputNumber = int(input('Think of a number between 1 and 5: '))
    generateNumber = random.randint(1,5)
    logic(inputNumber, generateNumber)
    print('The computer generated number is ', generateNumber)
    if inputNumber == generateNumber:
        score += 1
    print("score is ",score)
    




