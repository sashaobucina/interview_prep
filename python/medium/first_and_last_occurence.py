def searchRange(nums: list, target: int) -> list:
  if not nums or len(nums) < 1:
    return [-1, -1]

  targetRange = [-1, -1]
  leftIdx = insertionIndex(nums, target, True)
  
  if leftIdx == len(nums) or nums[leftIdx] != target:
    return targetRange

  targetRange[0] = leftIdx
  targetRange[1] = insertionIndex(nums, target, False) - 1

  return targetRange


def insertionIndex(nums: list, target: int, left: bool) -> int:
  lo, hi = 0, len(nums)
  while lo < hi:
    mid = (lo + hi) // 2
    if nums[mid] > target or (left and target == nums[mid]):
      hi = mid
    else:
      lo = mid + 1

  return lo

if __name__ == "__main__":
  arr = [1, 2, 8, 8, 8, 8, 8]
  print(searchRange(arr, 8))