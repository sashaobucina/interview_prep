from typing import List


def print_vertically(s: str) -> List[str]:
    """
    # 1324: Given a string s. Return all the words vertically in the same order in which they appear in s.

    Words are returned as a list of strings, complete with spaces when is necessary.
    (Trailing spaces are not allowed).

    Each word would be put on only one column and that in one column there will be only one word.
    """
    strs = s.split()
    m = len(max(strs, key=len))
    res = ["" for _ in range(m)]

    for s in strs:
        for i in range(m):
            if i < len(s):
                res[i] += s[i]
            else:
                res[i] += " "

    return [x.rstrip() for x in res]


if __name__ == "__main__":
    s = "HOW ARE YOU"
    expected = ["HAY", "ORO", "WEU"]
    assert print_vertically(s) == expected

    s = "TO BE OR NOT TO BE"
    expected = ["TBONTB", "OEROOE", "   T"]
    assert print_vertically(s) == expected

    s = "CONTEST IS COMING"
    expected = ["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]
    assert print_vertically(s) == expected

    print("Passed all tests!")
