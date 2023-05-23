# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Define Math Operations
class MathOperations:
    def __init__(self):
        self.operation = ""
        self.num1 = 0
        self.num2 = 0
        self.result = 0

    # Ask the user for the operation to perform
    def get_operation(self):
        while True:
            self.operation = input("Please choose a math operation (+, -, *, /): ")
            if self.operation in ("+", "-", "*", "/"):
                break
            else:
                print("\033[31mError: Invalid operation.\033[0m")
    # Ask the user for two numbers
    def get_numbers(self):
        while True:
            try:
                self.num1 = float(input("Enter the first number: "))
                self.num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("\033[31mError: Invalid input. Please enter a number.\033[0m")

    # Calculate the result based on the chosen operation
    def calculate_result(self):
        if self.operation == "+":
            self.result = self.num1 + self.num2
        elif self.operation == "-":
            self.result = self.num1 - self.num2
        elif self.operation == "*":
            self.result = self.num1 * self.num2
        elif self.operation == "/":
            try:
                if self.num2 == 0:
                    raise ZeroDivisionError("\033[31mError: Cannot divide by zero. \033[0m")
            except ZeroDivisionError as e:
                print(f"{str(e)} Please enter a second number again.")
                self.num2 = float(input("Enter the second number: "))
            self.result = self.num1 / self.num2

    # Print the result
    def print_result(self):
        print("Result:", self.result)