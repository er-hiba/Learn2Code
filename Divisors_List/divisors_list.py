# Input: Ask the user to enter a positive non-null integer
n = int(input("Enter a positive non-null integer: "))

i = 1     # Initialize a variable to start testing divisors at 1

                              # Start a loop to find and print divisors
while i <= n :                # Continue the loop until i reaches n
    if n % i == 0 :           # Check if i is a divisor of n
        print(i)              # If it is a divisor, print it
    i += 1                    # Move on to the next number
