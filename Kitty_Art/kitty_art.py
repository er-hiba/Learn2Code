#This program creates a cute kitty figure using basic ASCII characters, 
#with indentation for a cleaner display.

# Define ASCII art components for the kitty
ears = " A_-_A"      # Kitty's ears
eyes = "/ , , \\"    # Kitty's eyes
nose = "\\ =t= /"    # Kitty's nose
body = " |~x~|"      # Kitty's body
arms = " ||-||"      # Kitty's arms
legs = " [( )]"      # Kitty's legs
tb = "\t"            # Tab character for indentation

# Print the kitty art with indentation and add a new line between the title "Kitty" and the ASCII art.
print("Kitty :", "\n")
print(tb*2,ears)
print(tb*2,eyes)
print(tb*2,nose)
print(tb*2,body)
print(tb*2,arms)
print(tb*2,legs)
