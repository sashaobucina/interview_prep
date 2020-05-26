vowels = {"a", "e", "i", "o", "u"}


def max_vowels(s: str, k: int) -> int:
    """
    # 1456: Return the maximum number of vowel letters in any substring of s with length k.

    Constraints:
    - s consists of lowercase English letters.
    - 1 <= k <= s.length
    """
    longest = 0
    for i in range(k):
        if s[i] in vowels:
            longest += 1

    count = longest
    for i in range(len(s) - k):
        if longest == k:
            return longest

        if s[i] in vowels:
            count -= 1
        if s[i+k] in vowels:
            count += 1
        longest = max(longest, count)

    return longest


if __name__ == "__main__":
    s = "weallloveyou"
    print(max_vowels(s, 7))     # Expected: 4

    s = "rhythms"
    print(max_vowels(s, 4))     # Expected: 0

    s = "aieou"
    print(max_vowels(s, 3))     # Expected: 3
