# This program checks if a user-entered integer is a prime number. It calculates
# the number of divisors for the entered number and determines its primality
# based on the count of divisors. A prime number is defined as having exactly
# two divisors: 1 and itself. The code also includes error handling to manage
# cases where the user inputs a non-integer value.


try:
    # Input: Ask the user to enter an integer
    N = int(input("Enter an integer: "))

    # Initialize a counter for divisors
    divisor_count = 0

    # Loop through numbers from 1 to N
    for n in range (1, N+1):
        # Calculate the remainder when N is divided by n
        remainder = N % n
        # If the remainder is 0, it's a divisor
        if remainder == 0 :
            # Increase the divisor count for each divisor found
            divisor_count += 1

    # Check if the number has exactly 2 divisors
    if divisor_count == 2:
        # Output a message indicating that the number is prime
        print(N, "is a prime number")
    else :
        # Output a message indicating that the number is not prime
        print(N, "is a composite number")

# Handle the case where the user didn't enter a valid integer
except ValueError:
    print("This number is non-integer, it can't be prime.")
