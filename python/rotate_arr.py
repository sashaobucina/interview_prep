def rotate(nums: list, k: int) -> None:
  k %= len(nums)
  _reverse(nums, 0, len(nums) - 1)
  _reverse(nums, 0, k - 1)
  _reverse(nums, k, len(nums) - 1)

def _reverse(nums: list, start: int, end: int) -> None:
  while start < end:
    temp = nums[start]
    nums[start] = nums[end]
    nums[end] = temp
    start += 1
    end -= 1

if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5, 6, 7]
  rotate(arr, 3)
  print(arr)