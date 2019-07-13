"""
"""
def lis(nums: list) -> int:
  n = len(nums)
  table = [1] * n

  for i in range(1, n):
    for j in range(0, i):
      if nums[i] > nums[j] and table[i] < table[j] + 1:
        table[i] = table[j] + 1

  maximum = 0
  for i in range(n):
    maximum = max(maximum, table[i])
  return maximum

if __name__ == "__main__":
  arr = [10, 9, 2, 5, 3, 7, 101, 18]
  print(lis(arr))