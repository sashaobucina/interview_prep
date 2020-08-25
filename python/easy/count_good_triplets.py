from typing import List


def count_good_triplets(arr: List[int], a: int, b: int, c: int) -> int:
    """
    # 1534: Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

    A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
        - 0 <= i < j < k < arr.length
        - |arr[i] - arr[j]| <= a
        - |arr[j] - arr[k]| <= b
        - |arr[i] - arr[k]| <= c

    Where |x| denotes the absolute value of x.

    Return the number of good triplets.
    """
    count = 0
    N = len(arr)
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    count += 1

    return count


if __name__ == "__main__":
    arr = [3, 0, 1, 1, 9, 7]
    assert count_good_triplets(arr, 7, 2, 3)

    arr = [1, 1, 2, 2, 3]
    assert count_good_triplets(arr, 0, 0, 1) == 0

    print("Passed all tests!")
