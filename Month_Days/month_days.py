# Input: Ask the user to enter a month in numbers
M = int(input("Enter the month's number: "))

# Check the month number and display the number of days in that month.
if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12 :
    print("This month has 31 days.")
elif M == 4 or M == 6 or M == 9 or M == 11 :
    print("This month has 30 days.")
elif M == 2 :
    print("February has 28 or 29 days.")
else:
    print("Invalid month number entered.")
