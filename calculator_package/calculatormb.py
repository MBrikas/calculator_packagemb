class Calculator:
    ''' This calculator is designed to carry out fundamental arithmetic operations and calculate roots.
    It comes equipped with a memory feature, allowing it to store previous calculation results '''

    def __init__(self):
        ''' This function sets up the Calculator with an initial memory value of 0 '''
        self.memory = 0

    def add(self, num):
        ''' It increments the current memory value by a given number. '''
        self.memory += num
        return self.memory

    def subtract(self, num):
        ''' It subtracts a given number from the current memory value. '''
        self.memory -= num
        return self.memory

    def multiply(self, num):
        ''' This function multiplies the current memory value by a given number '''
        self.memory *= num
        return self.memory

    def divide(self, num):
        ''' This function divides the current memory value by a given number.. '''
        if num != 0:
            self.memory /= num
            return self.memory
        else:
            raise ValueError("Division by zero is not allowed!")

    def root(self, n):
        ''' This function calculates the nth root of the current memory value. '''
        if n >= 0:
            self.memory = round(self.memory ** (1 / n),3)
            return self.memory
        else:
            raise ValueError("Calculating a negative root is not possible!")

    def reset_memory(self):
        ''' Reset the calculator's memory to zero. '''
        self.memory = 0

# Helper function to get user input for numbers
def get_input_number():
    while True:
        try:
            num = float(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main program to showcase Calculator functionality
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
