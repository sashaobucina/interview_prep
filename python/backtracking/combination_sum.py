def combinationSum(candidates: list, target: int) -> list:
  def backtrack(subset = [], sum = 0, n = 0):
    if sum == target:
      ans.append(subset)
      return
    for i in range(n, len(candidates)):
      num = candidates[i]
      if sum + num <= target:
        backtrack(subset + [num], sum + num, i)
  ans = []
  if candidates:
    for i, num in enumerate(candidates):
      backtrack([num], num, i)
  return ans

if __name__ == "__main__":
  arr = [6, 3, 7, 2]
  print(combinationSum(arr, 8))