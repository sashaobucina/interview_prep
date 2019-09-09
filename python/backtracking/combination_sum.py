"""
iven a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

NOTE: Time complexity is O(n!)
"""
def combination_sum(candidates: list, target: int) -> list:
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


"""
Given a collection of candidate numbers (candidates) and a target number (target), find all 
unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

NOTE:
  - All numbers (including target) will be positive integers.
  - The solution set must not contain duplicate combinations.
"""
def combination_sum_II(candidates: list, target: int) -> list:
  candidates.sort()
  sums, n = [], len(candidates)

  def find_combos(subset: list, sum: int, start: int) -> None:
    if sum == target:
      sums.append(subset)
      return

    for i in range(start, n):
      if i > start and candidates[i] == candidates[i - 1]:
        continue
      num = candidates[i]
      if sum + num <= target:
        find_combos(subset + [num], sum + num, i + 1)

  find_combos([], 0, 0)
  return sums

if __name__ == "__main__":
  arr = [6, 3, 7, 2]
  print(combination_sum(arr, 8))

  arr2 = [10, 1, 2, 7, 6, 1, 5]
  print(combination_sum_II(arr2, 8))