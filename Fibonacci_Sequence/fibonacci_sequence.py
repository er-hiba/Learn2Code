# Prompt the user to input an integer greater than or equal to 2.
while True :
    n = int(input("Enter an integer greater than or equal to 2: "))
    if n >= 2 :
        break

# Initialize the first two Fibonacci sequence values
a = 0
b = 1

# Generate and print Fibonacci numbers until reaching n.
while a < n :
    print(a)
    # Calculate the next Fibonacci number and update a and b.
    c = b + a
    a = b
    b = c
