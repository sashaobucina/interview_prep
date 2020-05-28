from typing import List


def _swap(lst: List[int], idx1: int, idx2: int) -> None:
    """ Swap two elements in the list, given their indices. """
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]


def zigzag_sort(lst: List[int]) -> None:
    """
    Given an array of distinct elements, rearrange the elements of array in zig-zag fashion.
    The converted array should be in form a < b > c < d > e < f.

    Time complexity: O(n)
    """
    flag = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            if flag:
                _swap(lst, i, i+1)
        else:
            if not flag:
                _swap(lst, i, i+1)
        flag = not flag


if __name__ == "__main__":
    lst = [4, 3, 7, 8, 6, 2, 1]
    zigzag_sort(lst)
    assert lst == [3, 7, 4, 8, 2, 6, 1]

    print("Passed all tests!")
