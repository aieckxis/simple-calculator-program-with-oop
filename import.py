# Import the calculator.py
from calculator import MathOperations
# Create a MathOperations object
def main():
    math = MathOperations()

    while True:
        math.get_operation()
        math.get_numbers()
        math.calculate_result()
        math.print_result()
# Ask the user if they want to try again
# Call the main function to start the program
if __name__ == "__main__":
    main()