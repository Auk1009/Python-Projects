class Bank_Account:
    def __init__(self,account_holder: str,balence:float):
        self.account_holder = account_holder
        self.balence = balence

    def deposit(self,deposit):
        if deposit < 0:
            print('YOu cannot give a negative value')
        else:
            newBalence = deposit + self.balence
            self.balence = newBalence
            print(f"Current Balence: {newBalence}")

    def withdraw(self,withdraw):
        if withdraw>self.balence:
            print('You dont have that much money')
        elif withdraw < 0:
            print("You cannot give a negative value")
        else:
            newBalence = self.balence - withdraw
            self.balence = newBalence
            print(f"Current Balence: {newBalence}")

    def display_balence(self):
        print(f"Current Balence: {self.balence}")


    

myAccount = Bank_Account('Aryan',2000)
myAccount.deposit(1000)
myAccount.withdraw(500)
myAccount.display_balence()