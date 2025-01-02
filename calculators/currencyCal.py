def conversionToRupee(doller)-> float:
    doller = doller * 85
    return doller

def conversionToDoller(rupee)-> float:
    rupee = rupee/85
    return rupee


while True:
    userInput = int(input('d to r(1) or r to d(2)'))
    if userInput == 1:
        usdoller:float = float(input('convert doller to rupee:'))
        result = conversionToRupee(usdoller)
        print(f'dollers: {result}')
    elif userInput == 2:
        inr = float(input('conver rupee to doller'))
        result = conversionToDoller(inr)
        print(f'Rupee: {result}')


