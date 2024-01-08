class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def get_operation(self):
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ")
        return choice

    def calculate(self):
        while True:
            choice = self.get_operation()

            if choice == '5':
                break

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", self.add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", self.subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", self.multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", self.divide(num1, num2))
            else:
                print("Invalid input")

calculator = Calculator()
calculator.calculate()