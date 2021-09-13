"""An exercise in remainders and boolean logic."""

__author__ = "730529273"


choice: int = int(input("Enter ana int: "))
leftover_one: int = choice % 2
leftover_two: int = choice % 7
leftover_three: int = choice % 14
if leftover_three == 0:
    print("TAR HEELS")
else:
    if leftover_one == 0:
        print("TAR")
    else:
        if leftover_two == 0:
            print("HEELS")
        else:
            print("CAROLINA")
