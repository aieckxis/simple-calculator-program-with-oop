#Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Define Math Operations
class MathOpeations:
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
                print("Error: Invalid operation.")
# Ask the user for two numbers
    def get_numbers(self):
        while True:
            try:
                self.num1 = float(input("Enter the first number: "))
                self.num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Error: Invalid input. Please enter a number.")
# Calculate the result based on the chosen operation
# Print the result