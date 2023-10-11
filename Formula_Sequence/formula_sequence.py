# This program calculates and prints the value of U(n) based on the provided recursive formula.
# U(0) is initialized to 6, and the user is prompted to enter an integer 'n'.
# The program then iteratively calculates U(n) using the formula U(n+1) = 4 * U(n) + 10.


# Input: Ask the user to enter an integer 'n'
n = int(input("Enter an integer: "))

# Initialize U with the base case U(0) = 6
U = 6

# Calculate U(n) iteratively using the recursive formula
for i in range(1, n+1, 1):
    U = U * 4 + 10

# Output: Display the result
print("U of",n,"is:", U)
