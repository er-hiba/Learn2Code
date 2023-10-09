# This is a simple program that collects characters from the user to form
# a text. The characters are entered one at a time.
# The period ('.') entered to finish the input will not be displayed in the output. 
# Please note that it does not handle errors.

# Initialize an empty variable to store the characters
text = ""

# Continuously ask the user for input
while True:
    # Get a single character input from the user
    x = input("Enter a single letter, symbol, or space (or '.' to finish): ")

    # Check if the input is a period (.) to exit the loop
    if x == ".":
        break
    # Check if the input is a single character
    elif len(x) == 1:
        # Append the character to the text
        text += x
    else:
        # Provide an error message for invalid input
        print("Invalid input. Please enter only one character at a time.")

# Output: Display the entered text
print("The text you've entered is:", text)
