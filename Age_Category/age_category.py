# Input: Ask the user for the child's age
age = int(input("Enter the child's age: "))

# Check the age and print the corresponding category
if age == 6 or age == 7 :
    print("Youngster")
elif age == 8 or age == 9 :
    print("Pupil")
elif age == 10 or age == 11 :
    print("Junior")
elif age >= 12 :
    print("Cadet")
else :
    print("This child doesn't belong to any category.")
