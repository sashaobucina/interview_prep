from typing import List


def compress(chars: List[str]) -> int:
    """
    # 443: Given an array of characters, compress it in-place.

    The length after compression must always be smaller than or equal to the original array.

    Every element of the array should be a character (not int) of length 1.

    After you are done modifying the input array in-place, return the new length of the array.
    """
    anchor = wr = 0
    for r, ch in enumerate(chars):
        if r + 1 == len(chars) or chars[r + 1] != ch:
            chars[wr] = chars[anchor]
            wr += 1

            if r > anchor:
                for digit in str(r - anchor + 1):
                    chars[wr] = digit
                    wr += 1

            anchor = r + 1

    return wr


if __name__ == "__main__":
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    assert compress(chars) == 6
    assert chars[:6] == ["a", "2", "b", "2", "c", "3"]

    chars = ["a"]
    assert compress(chars) == 1
    assert chars[:1] == ["a"]

    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    assert compress(chars) == 4
    assert chars[:4] == ["a", "b", "1", "2"]

    print("Passed all tests!")
