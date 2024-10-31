def massConverter( num1, result, unitIdentifier):
    if unitIdentifier == 'kg':
        result = float(num1)* 1000 
        result = str(result) + ' g'
        return result
    elif unitIdentifier == "g":
        result = float(num1)/ 1000 
        result = str(result) + ' Kg'
        return result 


try:
    num1 = float(input('Enter the Mass:'))
except ValueError as e:
    print("Enter the valid number") 
    exit
except Exception as e:
    print("Enter the valid mass") 
    exit
unitIdentifier = str(input('Mass Unit kg or g: '))
result = 0 

result = massConverter(num1,result, unitIdentifier)

   
print(result) 

    
