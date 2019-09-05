import heapq

"""
O(n + klogn)
"""
def kth_largest(arr: list, k: int) -> int:
  copy = arr.copy()
  heapq._heapify_max(copy)
  for i in range(k - 1):
    heapq._heappop_max(copy)
  return heapq._heappop_max(copy)

"""
O(nlogk)
"""
def kth_largest2(arr: list, k: int) -> int:
  subset = arr[:k].copy()
  heapq.heapify(subset)
  for i in range(k, len(arr)):
    top = heapq.heappop(subset)
    if arr[i] > top:
      heapq.heappush(subset, arr[i])
    else:
      heapq.heappush(subset, top)

  return heapq.heappop(subset)



if __name__ == "__main__":
  arr = [7, 4, 6, 3, 9, 1]
  print(kth_largest(arr, 2))    # expected: 7
  print(kth_largest2(arr, 2))   # expected: 7