# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2

# Prompt the user to enter the numbers and the operation
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
operation = input('Enter the operation (+, -, *, /): ')

# Call the calculate function and print the result
result = calculate(num1, num2, operation)
print(result)
