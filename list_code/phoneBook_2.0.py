class phoneBook:

    def __init__(self, name, age, number) -> None:
        self.name = name
        self.age = age
        self.number = number
    
    def __str__(self) -> str:
        return f"{self.name}, {self.age}, {self.number}"

phoneBookDict = {}

def addContact(phoneObj):
    phoneBookDict[phoneObj.name] = phoneObj
    print(phoneBookDict)

addContact("aryan")



        

