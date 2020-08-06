def length_of_longest_substring(s: str) -> int:
    """
    # 3: Given a string, find the length of the longest substring without repeating characters.

    This sol'n uses the sliding window approach, using a character map to check last occurence of that
    character.
    """
    N = len(s)
    ch_map = [0] * 128

    ans = 0
    i, j = 0, 0
    while j < N:
        if ch_map[ord(s[j])]:
            i = max(ch_map[ord(s[j])], i)

        ans = max(ans, j - i + 1)
        ch_map[ord(s[j])] = j + 1
        j += 1

    return ans


if __name__ == "__main__":
    assert length_of_longest_substring("a") == 1
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3

    print("Passed all tests!")
