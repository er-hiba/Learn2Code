# This program takes two numbers as input, performs various
#mathematical operations on them, and displays the results.

# Input: Ask the user to enter the first number
N1 = float(input("Enter a number: "))
# Input: Ask the user to enter the second number
N2 = float(input("Enter another number: "))

# Calculate and print the sum of the two numbers
print("The sum of the two numbers is:", N1 + N2)

# Calculate and print the difference between the two numbers
print("The difference of the two numbers is:", N1 - N2)

# Calculate and print the product of the two numbers
print("The product of the two numbers is:", N1 * N2)

# Calculate and print the average of the two numbers
print("The average is:", (N1 + N2) / 2)

# Check if the second number (N2) is not equal to zero to avoid division by zero
if N2 != 0:
    # Calculate and print the integer quotient of the division
    print("The integer quotient of the division is:", int(N1 // N2))
    
    # Calculate and print the real quotient of the division
    print("The real quotient of the division is:", N1 / N2)
    
    # Calculate and print the modulo (remainder) of the division
    print("The modulo is:", N1 % N2)
else:
    # Display a message if division by zero is attempted
    print("Division by 0 is impossible.")
