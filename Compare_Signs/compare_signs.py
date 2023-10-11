# Input: Ask the user for 2 numbers
A = float(input("Enter a number: "))
B = float(input("Enter another number: "))

# Check if the numbers are both positive or both negative
if (A > 0 and B > 0) or (A < 0 and B < 0) :
    print("The two numbers have the same sign.")

# Check if either number is zero
elif A == 0 or B == 0 :
    print("0 is neither positive nor negative")

# If none of the above conditions are met, the numbers have different signs
else :
    print("The two numbers have different signs.")
