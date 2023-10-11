# Input: Ask the user to enter the product's price excluding tax (IP) and its category
IP = float(input("Enter the initial price of the product: "))
category = input("Enter the category of the product (A, B or C): ")

# Check the category of the product to calculate the final price (FP) with VAT
match category:
    case "A":
        # If the category is "A," apply a 7% VAT rate
        FP = IP * (1 + 7/100)
    case "B":
        # If the category is "B," apply a 20% VAT rate
        FP = IP * (1 + 20/100)
    case "C":
        # If the category is "C," apply a 25% VAT rate
        FP = IP * (1 + 25/100)

# Output: Display the final price
print("The total price with VAT is: ", FP)
