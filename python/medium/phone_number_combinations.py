"""
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent.

This solution uses DFS / backtracking.

Note: '0' and '1' are not valid and wont be in digits string.
"""
def letterCombinations(digits: str) -> list:
  mapping = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
  }
  ans = []

  def backtrack(S = "", n = 0):
    if n == len(digits):
      ans.append(S)
      return
    for letter in mapping[digits[n]]:
      backtrack(S + letter, n + 1)

  if digits:
    backtrack()
  return ans

if __name__ == "__main__":
  print(letterCombinations('23'))