def valid_palindrome(s: str) -> bool:
    """
    # 680: 
    """
    i, j = 0, len(s) - 1

    def _palindrome(i: int, j: int) -> bool:
        return all(s[k] == s[j - k + i] for k in range(i, j))

    while i < j:
        if s[i] != s[j]:
            return _palindrome(i + 1, j) or _palindrome(i, j - 1)

        i += 1
        j -= 1

    return True


if __name__ == "__main__":
    assert valid_palindrome("aba")
    assert valid_palindrome("abca")

    print("Passed all tests!")
