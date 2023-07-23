class Calculator:
    ''' This is a calculator that can perform basic arithmetic operations and take roots.
    The calculator maintains its own memory to store the result of previous operations. '''

    def __init__(self):
        ''' This function initializes the Calculator with an initial memory value of 0. '''
        self.memory = 0

    def add(self, num):
        ''' It adds a number from the current memory value. '''
        self.memory += num
        return self.memory

    def subtract(self, num):
        ''' It Subtracts a number from the current memory value. '''
        self.memory -= num
        return self.memory

    def multiply(self, num):
        ''' This function multiplies the current memory value by a number. '''
        self.memory *= num
        return self.memory

    def divide(self, num):
        ''' This function divides the current memory value by a number. '''
        if num != 0:
            self.memory /= num
            return self.memory
        else:
            raise ValueError("Cannot divide by zero!")

    def root(self, n):
        ''' This function takes the nth root of the current memory value. '''
        if n >= 0:
            self.memory = round(self.memory ** (1 / n),3)
            return self.memory
        else:
            raise ValueError("Cannot calculate negative root!")

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
        print("Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Take Root")
        print("6. Reset Memory")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

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
            print("Invalid choice. Please choose a valid option.")
