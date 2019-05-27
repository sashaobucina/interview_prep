"""
Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order
of characters. No two characters may map to the same character but a character may map to itself.
"""
def is_isomorphic(s: str, t: str):
  if (len(s) != len(t)):
    return False
  mapping = {}
  char_set = set()
  for i in range(len(s)):
    if (s[i] not in mapping):
      if t[i] in char_set:
        return False
      mapping[s[i]] = t[i]
      char_set.add(t[i])
    else:
      if mapping[s[i]] != t[i]:
        return False
  return True

if __name__ == "__main__":
  print(is_isomorphic("ab", "aa"))