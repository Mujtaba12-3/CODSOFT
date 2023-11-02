# Prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operation (+, -, *, /): ")

# Function to perform arithmetic operations
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Division by zero is not allowed"
        return num1 / num2
    else:
        return "Invalid operator"

# Perform the calculation
result = calculate(num1, num2, operator)

# Display the result
if isinstance(result, float):
    print(f"Result: {num1} {operator} {num2} = {result:.2f}")
else:
    print(result)
