# This program calculates and displays the sum of powers of 10 from 0 to n

# Input: Ask the user to enter the value of n
n = int(input("Enter the value of n: "))

# Initialize a variable to store the sum
S = 0

# Iterate from 0 to n, inclusive
for i in range(0, n+1, 1):
    # Calculate and add 10 to the power of i to the sum
    S = S + 10**i

# Output: Display the sum of powers of 10
print("The sum is:", S)
