## Table of Contents

1. [Calculator Package purpose](#Purpose)
2. [Installation](#Installation)
3. [Getting Started](#Initiation)
4. [Create an instance of the Calculator class](#Initiation)
5. [Basic Usage](#Usage)
    1. [Addition](#Function)
    2. [Subtraction](#Function)
    3. [Multiplication](#Function)
    4. [Division](#Function)
    5. [Taking the nth root](#Function)
    6. [Resetting the memory](#Function)
6. [Usage Example](#Example)
7. [Author](#Author)

# Calculator Package

The Calculator package is a Python class that provides basic arithmetic operations and the ability to take roots. The calculator also maintains its own memory to store the result of previous operations.

## Installation

To use the Calculator package, you can install it via pip:

```bash
pip install -i https://test.pypi.org/simple/ calculatormb
```
## Getting Started
You can import the Calculator class into your Python script or interactive session like this:
```python
from calculator_package.calculatormb import Calculator
```
## Create an instance of the Calculator class:
```python
calculator = Calculator()
```
## Basic Usage
The Calculator class provides the following basic arithmetic operations:

### Addition:

- calculator.add(5) 
Output: 5 (Memory: 5)

- calculator.add(3)
Output: 8 (Memory: 8)

### Subtraction:
- calculator.subtract(3)
Output: 5 (Memory: 5)

- calculator.subtract(2)
Output: 3 (Memory: 3)

### Multiplication:
- calculator.multiply(2)
Output: 6 (Memory: 6)

- calculator.multiply(4)
Output: 24 (Memory: 24)

### Division:
 - calculator.divide(4)
Output: 6.0 (Memory: 6.0)

 - calculator.divide(2)
Output: 3.0 (Memory: 3.0)

Note: Division by zero will raise a ValueError.

### Taking the nth root:
 - calculator.root(2)
Output: 1.732 (Memory: 1.732)

 - calculator.root(3)
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
```python
if __name__ == "__main__":
    calculator = Calculator()

    while True:
        print(f"\nMemory: {calculator.memory}")
        print("Available choices:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Calculate Root")
        print("6. Reset Memory")
        print("7. Exit")

        choice = input("Please enter your selection (1-7): ")

        if choice == '1':
            num = float(input("Enter a number: "))
            print(f"Result: {calculator.add(num)}")
        elif choice == '2':
            num = float(input("Enter a number: "))
            print(f"Result: {calculator.subtract(num)}")
        elif choice == '3':
            num = float(input("Enter a number: "))
            print(f"Result: {calculator.multiply(num)}")
        elif choice == '4':
            num = float(input("Enter a number: "))
            try:
                print(f"Result: {calculator.divide(num)}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            n = float(input("Enter the root value: "))
            try:
                print(f"Result: {calculator.root(n)}")
            except ValueError as e:
                print(e)
        elif choice == '6':
            calculator.reset_memory()
            print("Memory reset.")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid selection. Please choose a valid option.")
```
### Author
Mazvydas Brikas