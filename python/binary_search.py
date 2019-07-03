def binary_search(n: list, target: int) -> int:
  lo, hi = 0, len(n)
  while lo < hi:
    mid = (lo + hi) // 2
    if n[mid] < target:
      lo = mid + 1
    else:
      hi = mid
  return lo

if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5, 6]
  print(binary_search(arr, 5))