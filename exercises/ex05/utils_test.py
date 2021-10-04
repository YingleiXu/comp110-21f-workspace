"""Unit tests for list utility functions."""
__author__ = "730529273"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single() -> None:
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_many() -> None:
    xs: list[int] = [1, 2, 3, 4]
    assert only_evens(xs) == [2, 4]


def test_sub_special() -> None:
    xs: list[int] = [1, 2, 3, 4]
    b: int = -1
    c: int = 5
    assert sub(xs, b, c) == [1, 4]


def test_sub_normal_1() -> None:
    xs_1: list[int] = [10, 20, 30, 40]
    b_1: int = 1
    c_1: int = 3
    assert sub(xs_1, b_1, c_1) == [20, 30]


def test_sub_normal_2() -> None:
    xs_2: list[int] = [20, 30, 40, 50, 60]
    b_2: int = 2
    c_2: int = 4
    assert sub(xs_2, b_2, c_2) == [40, 50]


def test_concat_empty() -> None:
    list_1: list[int] = []
    list_2: list[int] = [1, 2, 3, 4]
    assert concat(list_1, list_2) == [1, 2, 3, 4]


def test_concat_normal_1() -> None:
    list_1: list[int] = [1, 2, 3, 4]
    list_2: list[int] = [5, 6, 7, 8]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_normal_2() -> None:
    list_1: list[int] = [4, 5, 6, 7, 8]
    list_2: list[int] = [2, 3, 4, 5]
    assert concat(list_1, list_2) == [4, 5, 6, 7, 8, 2, 3, 4, 5]
