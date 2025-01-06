todolist = []

def addlist(item:str):
    todolist.append(item)
    print('Successful in adding to list')
    print(todolist)

def deletelist(item:str):
    todolist.remove(item)
    print('This item is checked from list')
    print(todolist)

def showlist():
    print(todolist)

running = True

while running:
    
    userinput = str(input('Add(1),check(2),show(3) items in list and to Exit(4): '))
    try:
        if userinput == '1':
            additem = input('Add item: ') 
            addlist(additem)
        elif userinput == '2':
            checkitem = input('check item: ')
            deletelist(checkitem)
        elif userinput == '3':
            showlist()
        elif userinput == '4':
            running = False
    except ValueError:
       print("Invalid input. Please enter a valid input")
    except Exception as e:
        print(f'An error has occured {e}')



