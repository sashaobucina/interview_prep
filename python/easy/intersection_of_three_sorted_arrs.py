from typing import List


def arrays_intersection(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    """
    # 1213: Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return 
    a sorted array of only the integers that appeared in all three arrays.
    """
    intersect = []
    a, b, c = 0, 0, 0
    while a < len(arr1) and b < len(arr2) and c < len(arr3):
        if arr1[a] == arr2[b] == arr3[c]:
            intersect.append(arr1[a])
            a += 1
            b += 1
            c += 1
            continue
        else:
            min_val = min(arr1[a], arr2[b], arr3[c])
            if arr1[a] == min_val:
                a += 1
            if arr2[b] == min_val:
                b += 1
            if arr3[c] == min_val:
                c += 1

    return intersect


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    assert arrays_intersection(arr1, arr2, arr3) == [1, 5]

    print("Passed all")
