import random

def logic(userInput,computerInput):
    
    if computerInput =='rock' and userInput =="paper" :
        result = 'User Won'
    elif computerInput=='rock' and userInput=='scissor':
        result = 'Computer Won'
    elif computerInput =='rock' and userInput=='rock':
        result = 'Tie'

    if computerInput=='paper' and userInput =='scissor':
        result = 'User Won'
    elif computerInput=='paper' and userInput == "rock":
        result = 'Computer Won' 
    elif computerInput=='paper' and userInput == 'paper':
        result='Tie'

    if computerInput=="scissor" and userInput=='rock':
        result = 'User Won'
    elif computerInput=="scissor" and userInput=="paper":
        result = 'Computer Won'
    elif computerInput=='scissor' and userInput=='scissor':
        result='Tie'
    
    return result

def aryan(name):
    print('Hello Aryan')  
  
rsplist=["rock","paper","scissor"]
computerInput=random.choice(rsplist)
userInput=input("User input: ")
print('Computer input:'+ computerInput)
print(logic(userInput,computerInput))


  



        













