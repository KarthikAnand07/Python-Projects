def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


def get_input():
    operation = input("Select operation (+, -, *, /): ")
    if operation in ['+', '-', '*', '/']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return operation, num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values. ")
            return None, None, None
    else:
        print("Invalid operation. Please select a valid operation.")
        return None, None, None


def calculate(operation, num1, num2):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)


def display_result(operation, num1, num2, result):
    print(f"The result of {num1} {operation} {num2} is: {result}")


def main():
    while True:
        operation, num1, num2 = get_input()
        if operation:
            result = calculate(operation, num1, num2)
            display_result(operation, num1, num2, result)
        cont = input("Do you want to perform another calculation? (yes/no): ")
        if cont.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
