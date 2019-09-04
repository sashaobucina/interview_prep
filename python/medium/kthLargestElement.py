import heapq

def kth_largest(arr: list, k: int) -> int:
  heapq._heapify_max(arr)
  for i in range(k - 1):
    heapq._heappop_max(arr)
  return heapq._heappop_max(arr)


if __name__ == "__main__":
  arr = [7, 4, 6, 3, 9, 1]
  print(kth_largest(arr, 2))