import random

def logic(user:int,computer:int):
    try:
        if user == computer:
            print('correct')
            print(user)
            print(computer)
        elif user != computer:
            print('wrong')
            print(user)
            print(computer)
    except ValueError:
        print('enter a string')

while True:
    userInput: int = int(input('guess a number between 1 to 5 '))
    compInput : int = random.randint(1,5)
    logic(userInput,compInput)