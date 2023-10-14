# Revenue Calculation
# This is a program that calculates Revenue based on Total Units Sold Method
#and displays it with the currency symbol.

# Input: Ask the user to enter the total number of units sold.
T = int(input("Enter the total number of units sold: "))

# Input: Ask the user to enter the price per unit.
P = float(input("Enter the price per unit: "))

# Input: Ask the user to enter the currency symbol.
Symbol = input("Enter the currency symbol: ")

# Calculate the revenue.
R = T * P

# Output: Display the revenue with the currency symbol.
# The currency symbol will be placed before the amount.
# The revenue is formatted with two decimal places for clarity.
print("The revenue is:",Symbol, round(R, 2))

