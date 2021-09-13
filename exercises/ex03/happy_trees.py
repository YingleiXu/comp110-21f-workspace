"""Drawing forests in a loop."""

__author__ = "730529273"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
i: int = 0
depth: int = int(input("Depth: "))
if depth <= i:
    print("")
while i < depth:
    print(TREE * i)
    i += 1
print(TREE * depth)
