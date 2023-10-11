# Input: Ask the user to input coefficients for a quadratic equation.
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate the discriminant (d) of the quadratic equation.
d = (b**2) - 4*a*c

# Check if the discriminant is negative, indicating no real solutions.
if d < 0 :
    print("The equation has no real solutions.")

# Check if the discriminant is zero, indicating a unique real solution.
elif d == 0 :
    x = - b / (2 * a)
    # Ouput: Display the solution rounded to three decimal places.
    print("The equation has a unique real solution: x =",round(x, 3))

# If the discriminant is positive, calculate and display two real solutions rounded to three decimal places.
else :
    x1 = (- b - d**0.5) / (2 * a)
    x2 = (- b + d**0.5) / (2 * a)
    print("The solutions of the equation are: x1 =", round(x1, 3), "and x2 =", round(x2, 3))
