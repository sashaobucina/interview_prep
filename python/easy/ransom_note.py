from collections import Counter


def can_construct(ransom: str, magazine: str) -> bool:
    """
    # 383: Given an arbitrary ransom note string and another string containing letters from all the magazines, 
    write a function that will return true if the ransom note can be constructed from the magazines; 
    otherwise, it will return false.

    Each letter in the magazine string can only be used once in your ransom note.
    """
    d = Counter(magazine)
    for ch in ransom:
        if ch not in d or d[ch] == 0:
            return False
        d[ch] -= 1

    return True


if __name__ == "__main__":
    ransom = "bg"
    magazine = "fajkngskjhqrbfdakmg"
    assert can_construct(ransom, magazine)

    ransom = "aa"
    magazine = "ab"
    assert not can_construct(ransom, magazine)

    print("Passed all tests!")
