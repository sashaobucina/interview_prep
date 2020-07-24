"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all 
array elements equal, where a move is incrementing n - 1 elements by 1.
"""
def minMoves(nums: list) -> int:
  # Increasing n - 1 elements by 1 is same as decreasing the max element by 1.
  return sum(nums) - min(nums) * len(nums)

"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements 
equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
"""
def minMovesII(nums: list) -> int:
  nums.sort()
  count, i, j = 0, 0, len(nums) - 1
  while i < j:
    count += nums[j] - nums[i]
    i += 1
    j -= 1
  return count

if __name__ == "__main__":
  nums = [1, 2, 3, 5, 7]
  print(minMoves(nums))
  print(minMovesII(nums))