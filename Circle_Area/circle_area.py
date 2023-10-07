# This program effectively calculates and displays the area of a 
#circle while handling cases where the user enters a non-positive radius

# Import the math module to access the accurate value of pi
import math  

# Input: Ask the user to enter the radius of the circle.
r = float(input("Enter the radius of the circle: "))

# Ensure that the provided radius value is positive using a while loop.
while r < 0 :
    r = float(input("The radius can't be negative or null. Please enter a positive radius: "))

# Calculate the area of the circle using the accurate value of pi.
A = math.pi * r**2

# Output: Display the area of the circle with two decimal places.
print(f"The area of the circle is: {A: .2f}")
