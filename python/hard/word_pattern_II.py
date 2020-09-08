def word_pattern_match(pattern: str, s: str) -> bool:
    """
    # 291: Given a pattern and a string str, find if str follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
    """
    def _dfs(pattern, s, d, _d):
        if len(pattern) == 0 and len(s) > 0:
            return False
        if len(pattern) == len(s) == 0:
            return True

        ch = pattern[0]
        for end in range(1, len(s) - (len(pattern) - 1) + 1):
            substr = s[:end]
            if ch not in d and substr not in _d:
                d[ch] = substr
                _d[substr] = ch

                if _dfs(pattern[1:], s[end:], d, _d):
                    return True

                del d[ch]
                del _d[substr]
            elif ch in d and d[ch] == substr:
                if _dfs(pattern[1:], s[end:], d, _d):
                    return True

        return False

    return _dfs(pattern, s, d={}, _d={})


if __name__ == "__main__":
    assert word_pattern_match("abab", "redblueredblue")
    assert word_pattern_match("aaaa", "asdasdasdasd")
    assert not word_pattern_match("aabb", "xyzabcxyzabc")

    print("Passed all tests!")
