"""Challenge Question #1."""
__author__ = "730529273"
choice: int = int(input("Enter a number: "))

# Implement this logic
# Print A when choice < 25
# Print B when choice >= 25 and < 50
# Print C when choice > 75
# Print D when choice >= 50 and <= 75
if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice > 75:
            print("C")
        else:
            print("D")  
