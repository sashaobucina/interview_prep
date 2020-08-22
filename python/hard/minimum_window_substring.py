from collections import Counter


def min_window(s: str, t: str) -> str:
    """
    # 76: Given a string S and a string T, find the minimum window in S which will contain all the 
    characters in T in complexity O(n).
    """
    if not t or not s:
        return ""

    ans = ""
    n = len(s)

    t_count = Counter(t)
    required = set(t)

    # find first window containing substring
    i = 0
    while i < n and required:
        ch = s[i]
        if ch in t_count:
            t_count[ch] -= 1
            if t_count[ch] == 0:
                required.remove(ch)

        i += 1

    # if more chars from substring required, substring not found in s
    if required:
        return ""

    ans = s[:i]
    start, end = 0, i

    def _minimize_window():
        nonlocal start
        while start < n:
            if s[start] in t_count:
                if not t_count[s[start]]:
                    break
                else:
                    t_count[s[start]] += 1

            start += 1

        if end - start < len(ans):
            return s[start:end]
        return ans

    while end < n:
        # minimize the substring
        if not required:
            ans = _minimize_window()

        # add to count of chars needed if in substring
        if s[start] in t_count:
            t_count[s[start]] += 1
            if t_count[s[start]] > 0:
                required.add(s[start])

        # subtract from count of chars needed if in substring
        if s[end] in t_count:
            t_count[s[end]] -= 1
            if t_count[s[end]] == 0:
                required.remove(s[end])

        start += 1
        end += 1

    if not required:
        return _minimize_window()

    return ans


if __name__ == "__main__":
    s, t = "acbbaca", "aba"
    assert min_window(s, t) == "baca"

    s, t = "ADOBECODEBANC", "ABC"
    assert min_window(s, t) == "BANC"

    s, t = "abcabdebac", "cda"
    assert min_window(s, t) == "cabd"

    print("Passed all tests!")
