budgetDict = {
}
def AddExpense(key,expense):
    budgetDict[key] = float(expense)
    print(budgetDict)

def DelExpense(key):
    budgetDict.pop(key)
    print(budgetDict)

def showExpenses():
    print(budgetDict)
income = input('What is the you monthly salary?   ')
while True:
    userInput = input("type 1 to add an expense, 2 to delete an expense, 3 to show all your expenses:  ")

    try:
        if userInput == "1":
            userKey = input('What did you spend money on?  ').lower()
            userValue = float(input(f'Amount you spent on {userKey.upper()}: '))
            print('Expense Added')
            AddExpense(userKey, userValue)
    
        elif userInput == "2":
            duserKey = input('What expense do you want to delete?  ').lower()
            DelExpense(duserKey)
            print("Expense Deleted")
    
        elif userInput == '3':
         showExpenses()
    
        else:
            print("Please type options 1, 2, and 3")

    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

    
    if budgetDict.values() > income:
        print('Your spending too much for your income')
    elif budgetDict.values() < income:
        print('Good')