def backspace_compare(S: str, T: str) -> bool:
  def skip(source: str, ind: int) -> int:
    skip_count = 0
    while ind >= 0:
      if source[ind] == "#":
        skip_count += 1
        ind -= 1
      elif skip_count > 0:
          skip_count -= 1
          ind -= 1
      else:
          return ind
    return ind

  i, j = len(S) - 1, len(T) - 1
  while i >= 0 or j >= 0:
    i, j = skip(S, i), skip(T, j)
    if (i < 0 and j >= 0) or (j < 0 and i >= 0):
      return False
    if S[i] != T[j]:
      return False
    i -= 1
    j -= 1

  return True




if __name__ == "__main__":
  print(backspace_compare("ab#c", "ad#c"))    # expected: True