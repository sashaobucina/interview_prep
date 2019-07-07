"""
Solution uses backtracking. Only add a valid sequence by keeping track of left and
right parantheses.
"""
def generateParantheses(n: int) -> list:
  ans = []
  def backtrack(S = '', left = 0, right = 0):
    if len(S) == 2 * n:
      ans.append(S)
      return
    if left < n:
      backtrack(S + '(', left + 1, right)
    if right < left:
      backtrack(S + ')', left, right + 1)
  if n >= 0:
    backtrack()
  return ans

if __name__ == "__main__":
  print(generateParantheses(4))

