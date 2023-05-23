# Simple App Calculator - OOP Principles

This Python program is a **simple calculator application** that uses **object-oriented programming (OOP) principles.** It allows users to perform **basic math operations** like **addition, subtraction, multiplication, and division**. The MathOperations class handles user input, validates it, performs the requested operation, and displays the result. If the user tries to divide by zero, an error message is shown, and they can enter the second number again. The application continues until the user chooses to exit. It demonstrates the use of OOP to create a straightforward and functional calculator.

## Usage
Using Command Prompt: 

1. Open the Start menu and search for "Command Prompt".
2. Click on "Command Prompt" to open the command prompt window.
3. Use the cd command to navigate to the directory containing the script file. For example, if the script file is located in the "Documents" folder, type: cd Documents
4. Type the command python script_name.py to run the script. Replace "script_name.py" with the actual name of the script file.
5. Press Enter to run the script.
6. The script will run and follow the prompts to input the operation and two numbers.
7. If user attempt to divide by zero, an error message will be shown, and user will be asked to enter the second number again.
8. User can then choose to try again or exit.

Alternatively, you can also run the script using the Python IDLE environment:

1. Open the Start menu and search for "Python".
2. Click on "Python" to open the Python IDLE environment.
3. Click on "File" at the top of the window and select "Open".
4. Navigate to the directory containing the script file and select it.
5. Click on "Run" at the top of the window and select "Run Module" or press the F5 key.
6. The script will run and follow the prompts to input the operation and two numbers.
7. If user attempt to divide by zero, an error message will be shown, and user will be asked to enter the second number again.
8. User can then choose to try again or exit.

## Code Explanation

<img width="550" alt="image" src="https://github.com/aieckxis/simple-calculator-program-with-oop/assets/129574374/35cd49ea-556d-4cb2-a7d9-40ef0998ffdb">

The **MathOperations class** represents the calculator functionality. It has the following attributes:
- **operation**: Stores the chosen math operation (+, -, *, /).
- **num1**: Stores the first number entered by the user.
- **num2**: Stores the second number entered by the user.
- **result**: Stores the result of the calculation.

<img width="550" alt="image" src="https://github.com/aieckxis/simple-calculator-program-with-oop/assets/129574374/14216f14-dd0b-48c0-b1d4-93da0fa2a011">

The **get_operation()** method prompts the user to choose a math operation (+, -, *, /) and stores it in the operation attribute.

<img width="550" alt="image" src="https://github.com/aieckxis/simple-calculator-program-with-oop/assets/129574374/1932fd10-5736-4c82-a4c1-4fc35c536baf">

The **get_numbers()** method prompts the user to enter the first and second numbers. It validates the input to ensure valid numeric values.

<img width="550" alt="image" src="https://github.com/aieckxis/simple-calculator-program-with-oop/assets/129574374/873ee6fd-1a60-4c70-99d3-857f91363ade">

The **calculate_result()** method performs the actual calculation based on the chosen operation. It uses conditional statements to determine the operation and updates the result attribute accordingly. If division by zero is detected, it raises a **ZeroDivisionError** and prompts the user to enter the second number again.

<img width="550" alt="image" src="https://github.com/aieckxis/simple-calculator-program-with-oop/assets/129574374/1ae955eb-0d67-441a-aadb-fcba2455162d">

The **print_result()** method displays the calculated result on the screen.

<img width="550" alt="image" src="https://github.com/aieckxis/simple-calculator-program-with-oop/assets/129574374/51be272f-ced2-49e8-9d46-fcc4dc6d49fe">

Including in the **MathOperations class** from another file called **calculator.py**. This allows us to use the functionalities and methods defined in the **MathOperations class** in our current code file.

**NOTE:** It's important to ensure that the **calculator.py** file is present in the same directory and that it contains the correct definition of the **MathOperations class.** Otherwise, an import error may occur.

<img width="550" alt="image" src="https://github.com/aieckxis/simple-calculator-program-with-oop/assets/129574374/d73e4221-6bda-4ac8-9e60-f97539e71dcf">

The **main()** function is the entry point of the program. It creates an instance of the **MathOperations class** and enters a loop to repeatedly perform calculations based on user input. Within the loop, it calls the **get_operation(), get_numbers(), calculate_result(), and print_result()** methods of the **MathOperations** object.

<img width="550" alt="image" src="https://github.com/aieckxis/simple-calculator-program-with-oop/assets/129574374/dc6b731e-f92f-47ea-8c9d-58dc3dfc4a2d">

After displaying the result, the user is prompted whether they want to try again. If they choose not to continue, the program exits with a closing message.

<img width="550" alt="image" src="https://github.com/aieckxis/simple-calculator-program-with-oop/assets/129574374/ce682c68-1eab-411b-87c7-f2cadc2258e2">

And last, use the condition **_ _ name _ _** == "**_ _ main _ _**" to check if the script is being run directly as the main program. If it is true, we call the **main()** function. This allows the code inside the **main()** function to be executed when the script is run directly.

## Potential Improvements 

- Expand the calculator's functionality by including more operations like exponentiation, square root, and more.
- Include a history feature to store previous calculations for easy review and recall.
- Improve user prompts and instructions to make them more intuitive and user-friendly.
- Enhance input validation to handle invalid operations and non-numeric inputs.
