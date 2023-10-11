# Input: Ask for the age and gender of the resident
age = int(input("Enter the age of the resident: "))
gender = input("Enter the gender of the resident (M for male, F for female): ")

# Check if the resident is eligible for tax and display it
if (gender == "M" and age > 20) or (gender == "F" and 18 <= age <= 35 ):
    print("This resident is taxable.")
else :
    print("This resident is not taxable.")
