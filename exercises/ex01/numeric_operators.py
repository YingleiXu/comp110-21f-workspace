"""My numeric operators program for COMP110."""
__author__ = "730529273"
left_hand_side: str = input("What is Left-hand side? ")
right_hand_side: str = input("What is Right-hand side? ")
print("Left-hand side: " + left_hand_side)
print("Right-hand side: " + right_hand_side)
print(str(left_hand_side) + " ** " + str(right_hand_side) + " is " + str(int(left_hand_side) ** int(right_hand_side)))
print(str(left_hand_side) + " / " + str(right_hand_side) + " is " + str(int(left_hand_side) / int(right_hand_side)))
print(str(left_hand_side) + " // " + str(right_hand_side) + " is " + str(int(left_hand_side) // int(right_hand_side)))
print(str(left_hand_side) + " % " + str(right_hand_side) + " is " + str(int(left_hand_side) % int(right_hand_side)))