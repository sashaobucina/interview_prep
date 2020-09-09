def backspace_compare(S: str, T: str) -> bool:
    """
    # 844: Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

    Note that after backspacing an empty text, the text will continue empty.
    """
    def skip(s):
        indices = []

        skip = 0
        for ch in s[::-1]:
            if ch == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                indices.append(ch)

        return indices

    return skip(S) == skip(T)


if __name__ == "__main__":
    assert backspace_compare("ab#c", "ad#c")
    assert backspace_compare("ab##", "a#c#")
    assert backspace_compare("a##c", "#a#c")
    assert not backspace_compare("a#c", "b")

    print("Passed all tests!")
