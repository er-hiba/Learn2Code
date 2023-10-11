# Input: Ask the user for 2 numbers
A = float(input("Enter a number: "))
B = float(input("Enter another number: "))

# Check if both numbers have the same sign 
if (A > 0 and B > 0) or (A < 0 and B < 0) :
    # If they have the same sign, swap their values
    C = A
    A = B
    B = C
else :
    # If they have different signs, update the first number to the sum
    C = A
    A = C + B
    # Update the second number to the product
    B = C * B

# Output: Display the updated values of the numbers
print("The first number entered is now", A)
print("The second number entered is now", B)
