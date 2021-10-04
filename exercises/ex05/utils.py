"""List utility functions part 2."""
__author__ = "730529273"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """Return even numbers only."""
    i: int = 0
    xs_even: list[int] = []
    if len(xs) == 0:
        return []
    else:
        while i < len(xs):
            if xs[i] % 2 == 0:
                xs_even.append(xs[i])
            i += 1
    return xs_even


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Generate a list which is a subset of the given list, between the specified start index and the end index - 1."""
    list_returned: list[int] = []
    while len(a_list) == 0:
        if b > len(a_list) or c <= 0:
            return []
    if b < 0:
        list_returned.append(a_list[0])
    else:
        list_returned.append(a_list[b])
    if c > len(a_list):
        list_returned.append(a_list[len(a_list) - 1])
    else:
        list_returned.append(a_list[c - 1])
    return list_returned


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Concat two lists."""
    for number in list_2:
        list_1.append(number)
    return list_1


print(only_evens([1, 2, 3]))
print(only_evens([1, 5, 3]))
print(only_evens([4, 4, 4]))
a_list: list[int] = [1, 2, 3, 4]
print(sub(a_list, -1, 5))
number: int
list_input_1: list[int] = []
list_input_2: list[int] = [5, 6, 7, 8]
print(concat(list_input_1, list_input_2))