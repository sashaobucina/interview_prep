def min_remove_to_make_valid(s: str) -> str:
    """
    # 1249: Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that 
    the resulting parentheses string is valid and return any valid string.

    Formally, a parentheses string is valid if and only if:
        - It is the empty string, contains only lowercase characters, or
        - It can be written as AB (A concatenated with B), where A and B are valid strings, or
        - It can be written as (A), where A is a valid string.
    """
    ans = []

    stk = []
    actual_idx = 0
    for ch in s:
        if ch.isalpha():
            ans.append(ch)
            actual_idx += 1
        elif ch == "(":
            stk.append(actual_idx)
        else:
            if stk:
                ans.insert(stk.pop(), "(")
                ans.append(ch)
                actual_idx += 2

    return "".join(ans)


def min_remove_to_make_valid_better(s: str) -> str:
    """
    This sol'n guarantees a time complexity f O(n), but requires two passes.
    """
    stk = []
    status = [False for _ in range(len(s))]

    for i, ch in enumerate(s):
        if ch == "(":
            stk.append(i)
        elif ch == ")" and stk:
            status[stk.pop()] = status[i] = True
        elif ch.isalpha():
            status[i] = True

    return "".join([ch for i, ch in enumerate(s) if status[i]])


if __name__ == "__main__":
    assert min_remove_to_make_valid("lee(t(c)o)de)") == "lee(t(c)o)de"
    assert min_remove_to_make_valid_better("lee(t(c)o)de)") == "lee(t(c)o)de"

    assert min_remove_to_make_valid("a)b(c)d") == "ab(c)d"
    assert min_remove_to_make_valid_better("a)b(c)d") == "ab(c)d"

    assert min_remove_to_make_valid("))((") == ""
    assert min_remove_to_make_valid_better("))((") == ""

    assert min_remove_to_make_valid("(a(b(c)d)") == "a(b(c)d)"
    assert min_remove_to_make_valid_better("(a(b(c)d)") == "a(b(c)d)"

    print("Passed all tests!")
