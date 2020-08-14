from collections import Counter


def longest_palindrome(s: str) -> int:
    """
    # 409: Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

    This is case sensitive, for example "Aa" is not considered a palindrome here.

    NOTE: Assume the length of given string will not exceed 1,010.
    """
    counter = Counter(s)

    ans = 0
    odd = False
    for count in counter.values():
        if count % 2 == 0:
            ans += count
        else:
            ans += (count - 1)
            odd = True

    return ans + 1 if odd else ans


if __name__ == "__main__":
    assert longest_palindrome("abccccdd") == 7

    print("Passed all tests!")
