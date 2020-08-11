from typing import List


def bubble_sort(arr: List[int]) -> None:
    """
    Start from beginning and bubble up elements to end.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]


def insertion_sort(arr: List[int]) -> None:
    """
    Sort as if you were sorting cards.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def selection_sort(arr: List[int]) -> None:
    """
    Take the minimum element, and place it at the beginning of the sorted section.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]


def mergesort(arr: list) -> None:
    """
    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]

        # Merge the left and right subarrays
        mergesort(l)
        mergesort(r)

        # Merge the sorted subarrays together
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


def quicksort(arr: List[int]) -> None:
    """
    Based on pivot, maintain lo & hi pointers, and 

    Time complexity: O(nlogn) average, O(n^2) worst-case, O(n) best-case
    Space complexity: O(1)
    """
    def partition(lo: int, hi: int) -> int:
        i, j = lo, hi
        pivot = arr[lo]
        while i < j:
            while arr[i] <= pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1

            # swap so smaller element on left side, and larger element on right side
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # swap to get pivot to desired location
        arr[lo], arr[j] = arr[j], arr[lo]
        return j

    def _quicksort(lo: int, hi: int) -> None:
        if lo >= hi:
            return

        # partition array into smaller and larger halves based on a pivot point
        p = partition(lo, hi)

        # now in relation to pivot, left side is all smaller and right side is all larger
        _quicksort(lo, p - 1)
        _quicksort(p + 1, hi)

    _quicksort(0, len(arr) - 1)


if __name__ == "__main__":
    expected = [1, 4, 5, 6, 11, 12]

    arr = [11, 5, 4, 6, 12, 1]
    bubble_sort(arr)
    assert arr == expected

    arr = [11, 5, 4, 6, 12, 1]
    insertion_sort(arr)
    assert arr == expected

    arr = [11, 5, 4, 6, 12, 1]
    selection_sort(arr)
    assert arr == expected

    arr = [11, 5, 4, 6, 12, 1]
    mergesort(arr)
    assert arr == expected

    arr = [11, 5, 4, 6, 12, 1]
    quicksort(arr)
    assert arr == expected

    print("Passed all tests!")
