def remove_duplicates(S: str) -> str:
    """
    # 1047: Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent 
    and equal letters, and removing them.

    We repeatedly make duplicate removals on S until we no longer can.

    Return the final string after all such duplicate removals have been made.
    It is guaranteed the answer is unique.
    """
    ans = []
    for ch in S:
        if ans and ch == ans[-1]:
            ans.pop()
        else:
            ans.append(ch)

    return "".join(ans)


if __name__ == "__main__":
    S = "abbaca"
    assert remove_duplicates(S) == "ca"

    print("Passed all tests!")
