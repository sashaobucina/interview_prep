"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and 
a non-empty word in str.
"""
def wordPattern(pattern: str, str: str) -> bool:
  words = str.split()
  if len(words) != len(pattern):
    return False

  d, seen = {}, set()
  for i in range(len(words)):
    if (words[i] in seen and pattern[i] not in d) or (pattern[i] in d and d[pattern[i]] != words[i]):
      return False
    seen.add(words[i])
    d[pattern[i]] = words[i]
  return True

def wordPatternOpt(pattern: str, s: str) -> bool:
  words = s.split()
  if len(pattern) == len(words):
    return len(set(zip(words, pattern))) == len(set(pattern)) == len(set(words))
  else:
    return False

if __name__ == "__main__":
  print(wordPattern("aaaa", "dog cat dog dog"))   # expected: False
  print(wordPatternOpt("abaa", "dog cat dog dog"))    # expected: True