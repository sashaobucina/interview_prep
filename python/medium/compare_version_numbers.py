def compare_version(version1: str, version2: str) -> int:
    """
    # 165: Compare two version numbers version1 and version2.

    If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

    You may assume that the version strings are non-empty and contain only digits and the . character.

    The . character does not represent a decimal point and is used to separate number sequences.

    For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level 
    revision of the second first-level revision.

    You may assume the default revision number for each level of a version number to be 0. For example, 
    version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. 
    Its third and fourth level revision number are both 0.
    """
    def get_next_chunk(version, p, n):
        if p >= n:
            return p, 0

        end = p
        while end < n:
            if version[end] == ".":
                break
            end += 1

        return end + 1, int(version[p: end])

    n1, n2 = len(version1), len(version2)

    p1 = p2 = 0
    while p1 < n1 or p2 < n2:
        p1, i1 = get_next_chunk(version1, p1, n1)
        p2, i2 = get_next_chunk(version2, p2, n2)

        if i1 != i2:
            return 1 if i1 > i2 else -1

    return 0


if __name__ == "__main__":
    version1, version2 = "0.1", "1.1"
    assert compare_version(version1, version2) == -1

    version1, version2 = "7.5.2.4", "7.5.3"
    assert compare_version(version1, version2) == -1

    version1, version2 = "1", "1.000"
    assert compare_version(version1, version2) == 0

    print("Passed all tests!")
