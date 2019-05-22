def search_insert_position(nums: list, target: int) -> int:
  for index, num in enumerate(nums):
    if (target <= num):
      return index
  return len(nums)

if __name__ == "__main__":
  nums = [1, 3, 5, 6]
  print(search_insert_position(nums, 0))