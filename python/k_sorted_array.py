import heapq

"""
Given a k sorted array that is almost sorted such that each of the N elements may be misplaced by at most
k spaces from the correct order. Find a O(nlogk) solution using a heap.
"""
def sort_k_sorted_array(arr: list, k: int):
  subset = arr[:k+1]
  heapq.heapify(subset)

  index = 0
  for i in range(k+1, len(arr)):
    arr[index] = heapq.heappop(subset)
    heapq.heappush(subset, arr[i])
    index += 1

  while(len(subset) > 0):
    arr[index] = heapq.heappop(subset)
    index += 1

if __name__ == "__main__":
  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
  sort_k_sorted_array(arr, 2)
  print(arr)