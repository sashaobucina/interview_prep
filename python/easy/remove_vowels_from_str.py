def remove_vowels(S: str) -> str:
    """
    # 1119: Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
    """
    vowels = {"a", "e", "i", "o", "u"}

    ans = []
    for ch in S:
        if ch not in vowels:
            ans.append(ch)

    return "".join(ans)


if __name__ == "__main__":
    S = "leetcodeisacommunityforcoders"
    assert remove_vowels(S) == "ltcdscmmntyfrcdrs"

    S = "aeiou"
    assert remove_vowels(S) == ""

    print("Passed all tests!")
