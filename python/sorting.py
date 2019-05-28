""" Various O(n^2) sorting algorithms """

def bubble_sort(arr: list) -> None:
  n = len(arr)
  for i in range(n):
    for j in range(n - i - 1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j + 1] = arr[j+1], arr[j]

def insertion_sort(arr: list) -> None:
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key

if __name__ == "__main__":
  arr = [11, 5, 4, 6, 2]
  insertion_sort(arr)
  print(arr)