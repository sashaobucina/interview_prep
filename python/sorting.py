def bubble_sort(arr: list) -> None:
  n = len(arr)
  for i in range(n):
    for j in range(n - i - 1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j + 1] = arr[j+1], arr[j]

if __name__ == "__main__":
  arr = [1, 5, 4, 6, 2]
  bubble_sort(arr)
  print(arr)