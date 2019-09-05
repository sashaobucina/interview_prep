import heapq

def kth_smallest(arr: list, k: int):
  copy = arr.copy()
  heapq.heapify(copy)
  for i in range(k-1):
    heapq.heappop(copy)
  return heapq.heappop(copy)


def kth_smallest2(arr: list, k: int):
  neg_arr = [-x for x in arr]
  subset = neg_arr[:k]

  heapq.heapify(subset)
  for i in range(k, len(neg_arr)):
    top = heapq.heappop(subset)
    if neg_arr[i] > top:
      heapq.heappush(subset, neg_arr[i])
    else:
      heapq.heappush(subset, top)

  return -heapq.heappop(subset)



if __name__ == "__main__":
  arr = [7, 4, 6, 3, 9, 1]
  print(kth_smallest(arr, 3))   # expected: 4
  print(kth_smallest2(arr, 3))    # expected: 4