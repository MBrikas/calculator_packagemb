# Calculator Package

The Calculator package is a Python class that provides basic arithmetic operations and the ability to take roots. The calculator also maintains its own memory to store the result of previous operations.

## Installation

To use the Calculator package, you can install it via pip:

``bash
pip install calculator-package

## Getting Started
You can import the Calculator class into your Python script or interactive session like this:
''from calculator_package import Calculator

## Then, create an instance of the Calculator class:
calculator = Calculator()

## Basic Usage
The Calculator class provides the following basic arithmetic operations:

###Addition:

- result = calculator.add(5) 
Output: 5 (Memory: 5)

- result = calculator.add(3)
Output: 8 (Memory: 8)

### Subtraction:
- result = calculator.subtract(3)
Output: 5 (Memory: 5)

- result = calculator.subtract(2)
Output: 3 (Memory: 3)

### Multiplication:
- result = calculator.multiply(2)
Output: 6 (Memory: 6)

- result = calculator.multiply(4)
Output: 24 (Memory: 24)

### Division:
 - result = calculator.divide(4)
Output: 6.0 (Memory: 6.0)

 - result = calculator.divide(2)
Output: 3.0 (Memory: 3.0)

Note: Division by zero will raise a ValueError.

### Taking the nth root:
 - result = calculator.root(2)
Output: 1.732 (Memory: 1.732)

 - result = calculator.root(3)
Output: 1.368 (Memory: 1.368)

Note: Negative root or root of zero will raise a ValueError.

### Resetting the memory:
- calculator.reset_memory()
Memory reset to 0.

## Handling Invalid Input
The Calculator class handles invalid input:

If an invalid number is entered during an operation, the calculator will prompt for a valid number.
If division by zero or a negative root is attempted, a ValueError will be raised.

### Example

Here's an example of a simple interactive program using the Calculator package:

from calculator_package import Calculator

calculator = Calculator()

while True:

    print(f"\nMemory: {calculator.memory}")
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Take Root")
    print("6. Reset Memory")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    # Handle user choices based on the selected operation.
    

    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please choose a valid option.")

### Author
Mazvydas Brikas