
"""List utility functions."""
__author__ = "730529273"


def main() -> None:
    """Entrypoint of program."""
    numbers: list[int] = [1, 2, 3]
    print(all(numbers, 1))
    print(all([1, 1, 1], 2))
    print(all(numbers, 2))
    print(is_equal([1, 2, 3], [1, 2, 3]))
    print(is_equal([1, 1, 0], [1, 0, 1]))
    print(max([1, 2, 3]))
    print(max([100, 99, 98]))
    print(max([]))


def all(numbers: list[int], b: int) -> bool:
    """Iff b is found in the numbers, return true."""
    # Move through each int within the list.
    i: int = 0
    while i < len(numbers):
        item: int = numbers[i]
        if item == b:
            return True
            i += 1
    return False


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    if list_1 == list_2:
        return True
    return False


def max(a: list[int]) -> int:
    """This is a function which returns the maximun of a list."""
    counter: int = 0
    maximun: int = a[0]
    if len(a) == 0:
        raise ValueError("max() arg is an empty List")

    while counter < len(a) - 1:
        if maximun <= a[counter + 1]:
            maximun = a[counter + 1]
        counter += 1
    return maximun

 
if __name__ == "__main__":
    main()
