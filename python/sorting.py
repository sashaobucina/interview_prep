""" Various O(n^2) sorting algorithms """

"""
Start from beginning and bubble up elements to end.
"""
def bubble_sort(arr: list) -> None:
  n = len(arr)
  for i in range(n):
    for j in range(n - i - 1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j + 1] = arr[j+1], arr[j]
"""
Sort as if you were sorting cards.
"""
def insertion_sort(arr: list) -> None:
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key

"""
Take the minimum element, and place it at the beginning of the sorted section.
"""
def selection_sort(arr: list) -> None:
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i+1, n):
      if arr[min_idx] > arr[j]:
        min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx]

""" Various O(nlogn) sorting algorithms """

def mergesort(arr: list) -> None:
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

if __name__ == "__main__":
  arr = [11, 5, 4, 6, 12, 1]
  mergesort(arr)
  print(arr)