"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all 
array elements equal, where a move is incrementing n - 1 elements by 1.
"""
def minMoves(nums: list) -> int:
  # Increasing n - 1 elements by 1 is same as decreasing the max element by 1.
  return sum(nums) - min(nums) * len(nums)

if __name__ == "__main__":
  nums = [1, 2, 3, 5, 6]
  print(minMoves(nums))