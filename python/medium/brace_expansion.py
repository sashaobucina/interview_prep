"""
A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter 
is represented as is.  If there is more than one option, then curly braces delimit the options. 
For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.
"""
def expand(S: str) -> list:
  res = []
  # N = sum(1 for s in S if s.isalpha())

  def dfs(word: list, start: int):
    if start == len(S):
      res.append("".join(word))
      return

    if S[start] != '{':
      dfs(word + [S[start]], start + 1)
    else:
      letters = []
      while S[start] != "}":
        if S[start].isalpha():
          letters.append(S[start])
        start += 1

      letters.sort()
      for letter in letters:
        dfs(word + [letter], start + 1)

  dfs([], 0)
  return res

if __name__ == "__main__":
  print(expand("{a,b}c{d,e}f"))   # expected: ["acdf","acef","bcdf","bcef"]