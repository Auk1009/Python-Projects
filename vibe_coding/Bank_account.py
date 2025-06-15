import csv
from datetime import datetime
import os

class BankAccount:
    def __init__(self):
        self.csv_file = "bank_account.csv"
        self.accounts = self.load_accounts()

    def load_accounts(self):
        """Load all accounts from the CSV file"""
        accounts = {}
        if os.path.exists(self.csv_file):
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    accounts[row['Account Number']] = {
                        'holder': row['Account Holder'],
                        'type': row['Account Type'],
                        'balance': float(row['Balance']),
                        'last_transaction': row['Last Transaction Date']
                    }
        return accounts

    def save_accounts(self):
        """Save all accounts to the CSV file"""
        fieldnames = ['Account Number', 'Account Holder', 'Account Type', 'Balance', 'Last Transaction Date']
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for acc_num, details in self.accounts.items():
                writer.writerow({
                    'Account Number': acc_num,
                    'Account Holder': details['holder'],
                    'Account Type': details['type'],
                    'Balance': f"{details['balance']:.2f}",
                    'Last Transaction Date': details['last_transaction']
                })

    def create_account(self, holder_name, account_type):
        """Create a new bank account"""
        # Generate new account number
        acc_num = str(1001 + len(self.accounts))
        while acc_num in self.accounts:
            acc_num = str(int(acc_num) + 1)

        self.accounts[acc_num] = {
            'holder': holder_name,
            'type': account_type,
            'balance': 0.0,
            'last_transaction': datetime.now().strftime('%Y-%m-%d')
        }
        self.save_accounts()
        return acc_num

    def get_balance(self, account_number):
        """Get the balance of an account"""
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        return "Account not found"

    def deposit(self, account_number, amount):
        """Deposit money into an account"""
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            self.accounts[account_number]['last_transaction'] = datetime.now().strftime('%Y-%m-%d')
            self.save_accounts()
            return f"Deposited ${amount:.2f}. New balance: ${self.accounts[account_number]['balance']:.2f}"
        return "Account not found"

    def withdraw(self, account_number, amount):
        """Withdraw money from an account"""
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                self.accounts[account_number]['last_transaction'] = datetime.now().strftime('%Y-%m-%d')
                self.save_accounts()
                return f"Withdrawn ${amount:.2f}. New balance: ${self.accounts[account_number]['balance']:.2f}"
            return "Insufficient funds"
        return "Account not found"

    def display_account(self, account_number):
        """Display account details"""
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            return f"""
Account Details:
Account Number: {account_number}
Account Holder: {acc['holder']}
Account Type: {acc['type']}
Balance: ${acc['balance']:.2f}
Last Transaction: {acc['last_transaction']}
"""
        return "Account not found"

    def list_all_accounts(self):
        """List all accounts"""
        return "\n".join([f"Account {num}: {details['holder']} - ${details['balance']:.2f}"
                         for num, details in self.accounts.items()])

def main():
    bank = BankAccount()
    
    while True:
        print("\nBank Account Management System")
        print("1. Create New Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Display Account Details")
        print("6. List All Accounts")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            holder = input("Enter account holder name: ")
            acc_type = input("Enter account type (Savings/Checking): ")
            acc_num = bank.create_account(holder, acc_type)
            print(f"Account created successfully! Account number: {acc_num}")

        elif choice == '2':
            acc_num = input("Enter account number: ")
            balance = bank.get_balance(acc_num)
            print(f"Balance: ${balance:.2f}" if isinstance(balance, float) else balance)

        elif choice == '3':
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
                print(bank.deposit(acc_num, amount))
            except ValueError:
                print("Invalid amount")

        elif choice == '4':
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
                print(bank.withdraw(acc_num, amount))
            except ValueError:
                print("Invalid amount")

        elif choice == '5':
            acc_num = input("Enter account number: ")
            print(bank.display_account(acc_num))

        elif choice == '6':
            print("\nAll Accounts:")
            print(bank.list_all_accounts())

        elif choice == '7':
            print("Thank you for using the Bank Account Management System!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 