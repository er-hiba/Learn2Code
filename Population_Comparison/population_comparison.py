# This program calculates and prints the number of years it takes for the population of Agadir 
# to surpass the population of Marrakech, given their initial populations and growth rates.

# Initial populations of Marrakech (PM) and Agadir (PA)
PM = 1000000
PA = 500000
year = 0

# Continue looping while the population of Marrakech is greater than Agadir
while PM > PA :
    # Marrakech's population increases by 50,000 each year
    PM += 50000
    # Agadir's population increases by 8% each year
    PA += PA * 0.08
    year += 1

# Output the result indicating the number of years it takes for Agadir's population to surpass Marrakech's
print("In",year,"years the population of Agadir will surpass that of Marrakech.")
