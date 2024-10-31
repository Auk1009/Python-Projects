def isEven(userInput):
    if float(userInput)%2 == 0:
        result = 'even'
    else:
        result = 'odd'

    return result

# input = input('Range: ')

for i in range(11):
    evenOrOdd = isEven(i)
    if (evenOrOdd == 'even'):
        print(i,end=' ')

    




