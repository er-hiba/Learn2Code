# This program calculates the sum of the squares of the first n odd integers

n = int(input("Enter a number for the first odd integers: "))

S = 0    # Initialize a variable to store the sum of squares
i = 1    # Initialize a counter for all integers (starting from 1)
N = 0    # Initialize a counter for the number of odd integers

while True:
    if i%2 != 0 :             # if i is odd
        S = S + i**2          # Add the square of the odd integer to the sum
        N = N + 1             # Increase the count of odd integers
    i += 1                    # Move to the next integer
    if N == n :
        break                 # Exit the loop when the desired count of odd integers is reached

# Output: Display the sum
print("The sum of the squares of the first",n,"odd integers is:", S)
