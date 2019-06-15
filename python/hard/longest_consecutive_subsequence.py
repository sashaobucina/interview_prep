def longestConsecutive(nums: list) -> int:
  longestStreak = 0
  s = set(nums)

  for num in s:
    if num - 1 not in s:
      currNum, currStreak = num, 1
      while currNum + 1 in s:
        currNum += 1
        currStreak += 1
      longestStreak = max(longestStreak, currStreak)
  return longestStreak

if __name__ == "__main__":
  arr = [100, 4, 200, 1, 3, 2]
  print(longestConsecutive(arr))