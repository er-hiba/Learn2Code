# Input: Ask the user to enter how many copies were made
n = int(input("Enter the number of the copies made: "))

# Calculate the bill based on the number of copies

# If the number of copies is 10 or less, each copy costs 0.30 MAD
if n <= 10 :
    B = n * 0.30

# If the number of copies is between 11 and 30 (inclusive),
# the first 10 copies cost 0.30 MAD each, and the rest cost 0.25 MAD each
elif n > 10 and n <= 30 :
    B = 10 * 0.30 + (n - 10) * 0.25


# If the number of copies is over 30, the first 10 copies cost 0.30 MAD each,
#the next 20 cost 0.25 MAD each, and the remaining copies cost 0.20 MAD each
else :
    B = 10 * 0.30 + 20 * 0.25 + (n - 30) * 0.20

# Output: Display the bill
print("The bill for the copies is:", B, "MAD")
