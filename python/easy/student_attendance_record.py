def check_record(s: str) -> bool:
    """
    # 551: You are given a string representing an attendance record for a student. The record only contains 
    the following three characters:
        1) 'A' : Absent.
        2) 'L' : Late.
        3) 'P' : Present.

    A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) 
    or more than two continuous 'L' (late).

    You need to return whether the student could be rewarded according to his attendance record.
    """
    absents = 0
    lates = False

    for i, rec in enumerate(s):
        if rec == "A":
            absents += 1
        elif rec == "L":
            if len(s[i:i + 3]) == 3 and all([s[i] == "L" for i in range(i, i + 3)]):
                lates = True

        if absents > 1 or lates:
            return False

    return True


if __name__ == "__main__":
    assert check_record("PPALLP")
    assert not check_record("PPALLL")

    print("Passed all tests!")
