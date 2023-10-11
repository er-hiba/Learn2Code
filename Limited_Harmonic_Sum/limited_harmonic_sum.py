# This program calculates and displays the sum of the harmonic series up to the "n-th" term.
# The harmonic series is defined as 1/1 + 1/2 + 1/3 + ... + 1/n.

# Input: Ask the user to enter the value of n, the number of terms to sum.
n = int(input("Enter the value of n: "))

# Initialize the variable S to 0, which will store the sum.
S = 0

# Iterate from 1 to n, adding each term (1/i) to the sum S.
for i in range(1, n+1, 1) :
    S = S + (1/i)

# Output: Display the calculated sum.
print("The sum is: ",S)
