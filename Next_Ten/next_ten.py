# Input: Ask the user to enter an integer
N = int(input("Enter an integer: "))

# Use a for loop to iterate from N+1 to N+10, which will give us the next ten numbers
for i in range(N+1, N+11, 1) :
    # Print the current value of 'i', which represents the next number in the sequence
    print(i)
