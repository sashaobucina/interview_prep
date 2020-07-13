from typing import List


def replace_elements(arr: List[int]) -> List[int]:
    """
    # 1299: Given an array arr, replace every element in that array with the greatest element 
    among the elements to its right, and replace the last element with -1.

    After doing so, return the array.
    """
    _max = -1
    for i in range(len(arr) - 1, -1, -1):
        tmp = arr[i]
        arr[i] = _max
        _max = max(_max, tmp)

    return arr


if __name__ == "__main__":
    arr = [17, 18, 5, 4, 6, 1]
    assert replace_elements(arr) == [18, 6, 6, 6, 1, -1]

    print("Passed all tests!")
