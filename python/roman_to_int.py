"""
Note that input is guaranteed to be between 1 and 3999
"""
def roman_to_int(s: str) -> int:
  roman_to_numeral = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
  }

  res = i = 0
  while i < len(s):
    s1 = roman_to_numeral[s[i]]
    if i + 1 < len(s):
      s2 = roman_to_numeral[s[i+1]]
      if s1 < s2:
        res += s2 - s1
        i += 2
      else:
        res = res + s1
        i += 1
    else:
      res = res + s1
      i += 1
  return res

if __name__ == "__main__":
  print(roman_to_int('MMMCMXCIX'))