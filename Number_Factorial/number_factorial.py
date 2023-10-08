# This program calculates the factorial of a number entered by the user.
# It handles cases where the input is zero, negative, or very large (greater than 170),
# providing appropriate messages for each scenario.
# Please note that it does not handle non-integer input errors.
# The code does not utilize functions. Which makes it suitable for beginners.


# Input: Ask the user to enter a number (N)
N = int(input("Enter an number: "))

# Initialize a variable F to 1.
# This variable functions as an accumulator to calculate the factorial,
# and starting with 1 ensures that the initial value doesn't affect the multiplication process.
F = 1

if N == 0:
    print("The factorial of 0 is 1.")

elif N < 0:
    print("Factorial is undefined for negative numbers.")

elif N > 170:
    print("Factorial exceeds representational limits (Infinity).")

else:
    for i in range(1, N + 1, 1): # Loop from 1 to N (inclusive)

        F = F * i  # Calculate the factorial by multiplying F by each number from 1 to N

    print("The factorial of N is:", F)  # Output: Display the result of the factorial
