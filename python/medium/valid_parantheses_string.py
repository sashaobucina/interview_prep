from collections import deque


def check_valid_string(s: str) -> bool:
    """
    # 678: Given a string containing only three types of characters: '(', ')' and '*', write a function 
    to check whether this string is valid.

    We define the validity of a string by these rules:
        - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        - Any right parenthesis ')' must have a corresponding left parenthesis '('.
        - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or 
            an empty string.
        - An empty string is also valid.
    """
    stk = []
    stars = deque([])
    for i, ch in enumerate(s):
        if ch == "*":
            stars.append(i)
        elif ch == "(":
            stk.append(i)
        else:
            if not stk and not stars:
                return False
            elif not stk:
                stars.popleft()
            else:
                stk.pop()

    # fail fast
    if len(stars) < len(stk):
        return False

    i, j = 0, 0
    while i < len(stars) and j < len(stk):
        if stars[i] < stk[j]:
            i += 1
        else:
            i += 1
            j += 1

    return j == len(stk)


if __name__ == "__main__":
    assert check_valid_string("()")
    assert check_valid_string("(*)")
    assert check_valid_string(("(*))"))
    assert check_valid_string("(()()(())(*()()())**()()()()()((*()*))((*()*)")
    assert not check_valid_string("(())((())()()(*)(*()(())())())()((())(()(*")

    print("Passed all tests!")
