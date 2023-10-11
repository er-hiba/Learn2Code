# This program calculates the total amount Amal will have in her savings account on her nth birthday, 
# with her grandfather depositing 500 MAD on each birthday, and adding three times her age to the account.

# Take user input for the nth birthday.
n = int(input("Enter the number of Amal's birthday: "))

# Initialize a variable to keep track of the total amount.
S = 0

# Initialize the age to 1.
age = 1

# Iterate through birthdays and calculate the total amount
while age <= n :
    # Calculate the amount added on each birthday: 500 + age * 3.
    S = S + 500 + age*3

    # Increment the age for the next birthday.
    age += 1

# Print the total amount Amal will have on her nth birthday
print("The total amount Amal will have on her", n, "birthday is:", S, "MAD")
