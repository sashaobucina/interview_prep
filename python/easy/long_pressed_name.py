def is_long_pressed_name(name: str, typed: str) -> bool:
    """
    # 925: Your friend is typing his name into a keyboard. 
    Sometimes, when typing a character c, the key might get long pressed, and the character will be 
    typed 1 or more times.

    You examine the typed characters of the keyboard.  Return True if it is possible that it was your 
    friends name, with some characters (possibly none) being long pressed.
    """
    i, j = 0, 0
    while i < len(name) and j < len(typed):
        if name[i] != typed[j]:
            return False

        if i + 1 == len(name) or name[i] != name[i + 1]:
            while j + 1 < len(typed) and typed[j] == typed[j + 1]:
                j += 1
        
        j += 1
        i += 1

    return i == len(name) and j == len(typed)


if __name__ == "__main__":
    assert is_long_pressed_name("alex", "aalexxx")
    assert not is_long_pressed_name("alex", "aalexxxr")
    assert not is_long_pressed_name("saeed", "ssaaaedd")
    assert is_long_pressed_name("leelee", "lleeelee")
    assert is_long_pressed_name("laiden", "laiden")

    print("Passed all tests!")
