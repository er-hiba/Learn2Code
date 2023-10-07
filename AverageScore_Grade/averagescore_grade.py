#This program calculates the average of three input scores, validates them within the 
#range of 0 to 20, and assigns a grade based on the calculated average. 
#It then displays both the average score and the corresponding grade.

# Input: Ask the user to enter three scores and convert them to floats.
A = float(input("Enter your 1st score: "))
B = float(input("Enter your 2nd score: "))
C = float(input("Enter your 3rd score: "))

# Validation: Ensure the first score is within the valid range [0, 20].
while A < 0 or A > 20 :
    A = float(input("Reenter your first score: "))

# Validation: Ensure the second score is within the valid range [0, 20].
while B < 0 or B > 20 :
    B = float(input("Reenter your second score: "))

# Validation: Ensure the third score is within the valid range [0, 20].
while C < 0 or C > 20 :
    C = float(input("Reenter your third score: "))

# Calculate the average of the three valid scores.
Average = (A + B + C)/3

# Determine the grade based on the average score.
if Average >= 16 :
    Grade = "Excellent"
elif Average >= 14 :
    Grade = "Good"
elif Average >= 12 :
    Grade = "Fair"
elif Average >= 10 :
    Grade = "Poor"
else :
    Grade = "Very poor" # Average score < 10 is "Very poor"

# Output: Display the average score and assigned grade.
print("Average score: ",Average ,"Grade: ", Grade)
