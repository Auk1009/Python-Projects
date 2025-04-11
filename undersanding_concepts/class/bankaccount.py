class Bank_account:
    # accounts_list = []
    def __init__(self,account_holder,account_number,balence):
        self.account_holder = account_holder
        self.account_number = account_number
        self._balence = balence
        # Bank_account.accounts_list.append(self)

    def owner_account_entry_number(self,owner:str,account_number2:int):
        self.account_holder = owner
        self.account_number = account_number2
    
    def view_balence(self):
        return self._balence
    
    def deposit_money(self,deposite:int):
        newbalence = self._balence + deposite
        self._balence = newbalence
        return newbalence
    
    def withdraw_money(self,withdraw:int):
        if self.balence >= withdraw:
            newwithdraw = self.balence - withdraw
            self.balence = newwithdraw
            print(f"Your current balence after withdrawing {newwithdraw}")
        else:
            print('Not enough money')

    def change_accountnum(self,newaccountnumber):
        self.account_number = newaccountnumber
        print('Successfully changed')


aryan = Bank_account('Aryan',1097642,1000)
ram = Bank_account('Ram',1432234,50000)
while True:

    
    account = aryan

    userinput = int(input('view Balence(1), deposite money(2), withdraw money(3), change account number(4)'))

    if userinput == 1:
        Bank_account.view_balence(account)
    elif userinput == 2:
        deposite_money = int(input('Enter the amout of money to be deposited: '))
        Bank_account.deposit_money(account,deposite_money)
    elif userinput == 3:
        withdraw_money = int(input('Enter the amount of money to be withdrawed: '))
        Bank_account.withdraw_money(account,withdraw_money)
    elif userinput == 4:
        new_number = int(input('enter the new account number: '))
        Bank_account.change_accountnum(account,new_number)




        