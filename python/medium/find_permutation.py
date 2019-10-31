"""
By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a 
decreasing relationship between two numbers, 'I' represents an increasing relationship between two 
numbers. And our secret signature was constructed by a special integer array, which contains uniquely 
all the different number from 1 to n (n is the length of the secret signature plus 1). For example, 
the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by 
array [3,2,4] or [2,1,3,4], which are both illegal constructing special string that can't represent the 
"DI" secret signature.

On the other hand, now your job is to find the lexicographically smallest permutation of [1, 2, ... n] 
could refer to the given secret signature in the input.
"""
def findPermutation(s: str) -> list:
  res, stk = [], []
  n = len(s)

  for i in range(1, n + 1):
    if s[i - 1] == "I":
      res.append(i)
      while len(stk) > 0:
        res.append(stk.pop())
    else:
      stk.append(i)

  stk.append(n + 1)
  while len(stk) > 0:
    res.append(stk.pop())
  return res

def findPermutationBacktracking(s: str) -> list:
  res = []
  n = len(s)
  usedNums = [False] * (n+2)

  def backtrack(code, s, used, res):
    if len(code) == n + 1:
        res.append(code)
        return

    appropriateRange = range(code[-1], 0, -1) if s[0] == "D" else range(code[-1], n + 2)

    for i in appropriateRange:
      if not usedNums[i]:
        usedNums[i] = True
        backtrack(code + [i], s[1:], usedNums, res)
        usedNums[i] = False


  for i in range(1, n + 2):
    usedNums[i] = True
    backtrack([i], s, usedNums, res)
    usedNums[i] = False

    # check if we are done
    if len(res) > 0:
      return res[0]

  return []

if __name__ == "__main__":
  print(findPermutationBacktracking("DI"))    # expected: [2, 1, 3]
  print(findPermutation("IIIIIIDDDDIIIIIIII"))
  # expected: [1, 2, 3, 4, 5, 6, 11, 10, 9, 8, 7, 12, 13, 14, 15, 16, 17, 18, 19]