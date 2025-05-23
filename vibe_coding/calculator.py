class Calculator:
    def __init__(self):
        self.result = 0
        self.operations = {
            '1': self.add,
            '2': self.subtract,
            '3': self.multiply,
            '4': self.divide
        }

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        if y == 0:
            return "Error: Cannot divide by zero"
        self.result = x / y
        return self.result

    def display_menu(self):
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    def get_numbers(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Error: Please enter valid numbers")
            return None, None

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter choice (1/2/3/4/5): ")

            if choice == '5':
                print("Thank you for using the calculator!")
                break

            if choice in self.operations:
                num1, num2 = self.get_numbers()
                if num1 is not None and num2 is not None:
                    result = self.operations[choice](num1, num2)
                    print(f"\nResult: {result}")
            else:
                print("Invalid choice! Please try again.")

            print(f"Last calculation result: {self.result}")


if __name__ == "__main__":
    calc = Calculator()
    calc.run() 