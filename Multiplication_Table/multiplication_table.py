# This program takes an integer input from the user and then
# prints a multiplication table for that number from 0 to 10.
# It uses a for loop to iterate through the range of integers from 0 to 10
# and calculates and displays the products.

# Input: Ask the user to enter an integer (x)
x = int(input("Enter an integer: "))

# Loop through integers from 0 to 10 and print the multiplication table of the input number
for i in range(0, 11):
    # Calculate the product of i and x, and print it in the specified format
    print(i,"*",x,"=",i*x)
