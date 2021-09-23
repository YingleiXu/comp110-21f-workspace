"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730529273"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
randomized_result: int = randint(1, 4)
if randomized_result == 1:
    print("404 not found.")
else:
    if randomized_result == 2:
        print("A , smart, and loving person will be coming into your life.")
    else:
        if randomized_result == 3:
            print("What a good life.")
        else:
            print("Don't worry!")
print("Now, go spread positive vibes!")