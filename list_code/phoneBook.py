phoneDict = {}

def addItem(key,value):
    phoneDict[key] = value
    print(phoneDict)
    print('Successfully Added')

def deleteItem(key):
    for check in phoneDict:
        if key == check:
          print(phoneDict)
          phoneDict.pop(key)
          print('Successfully Removed')
          break
        else:
            print('Contact not found')  
    
    


def findItem(key):
    for check in phoneDict:
        if key == check:
            print(phoneDict)
            print("Successfully found")
            break
        else:
            print("Not Found")


while(True):
    UserInput = int(input("Press 1 to add a contact, Press 2 to delete a contact, Press any number to find a contact: "))
    if UserInput == 1:
        Name = str(input('Enter the persons name: '))
        PhoneNumber = str((input('Enter the phone number only 10 digits: ')))
        print(len(PhoneNumber))
        if len(str(PhoneNumber)) > 11:
            print('Please type only 10 digits')
        else:
            addItem(Name,PhoneNumber)   
    
    elif UserInput == 2:
        OldCon = str(input('Enter the contact you what to remove: '))
        deleteItem(OldCon)
    
    else:
        Find = input('Which contact do you what to find: ')
        findItem(Find)







