# This program is a simple calculator that performs basic arithmetic operations on two numbers.
# It prompts the user to input two numbers (A and B) and the desired mathematical operation (Op).
# Then, it calculates and displays the result.


# Input: Ask the user to enter a number(A)
A = float(input("Enter the first number: "))

# Input: Ask the user to enter another number(B)
B = float(input("Enter the second number: "))

# Input: Ask the user to enter the desired mathematical operation (Op)
Op = input("Enter + or - or * or / or % for the operation you want: ")

# Check which operation the user wants to perform
if Op == "+":
    # If the operator is "+", perform addition and print the result
    print("A + B is:", A + B)
elif Op == "-":
    # If the operator is "-", perform subtraction and print the result
    print("A - B is:", A - B)
elif Op == "*":
    # If the operator is "*", perform multiplication and print the result
    print("A * B is:", A * B)
elif Op == "/":
    # If the operator is "/", check if B is not zero to avoid division by zero
    if B != 0:
        # If B is not zero, perform division and print the result
        print("A / B is:", A / B)
    else:
        # If B is zero, inform the user that division by zero is not possible
        print("Division by zero is not possible.")
elif Op == "%":
    # If the operator is "%", check if B is not zero to avoid modulo by zero
    if B != 0:
        # If B is not zero, perform modulo and print the result
        print("A % B is:", A % B)
    else:
        # If B is zero, inform the user that modulo by zero is not possible
        print("Modulo by zero is not possible.")
else:
    # If the user entered an invalid operator, display an error message
    print("Invalid operator.")
