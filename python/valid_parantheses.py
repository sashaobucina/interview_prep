def valid_parantheses(s: str) -> bool:
    """
    # 20: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
    # determine if the input string is valid.

    An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Note that an empty string is also considered valid.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    stack = []
    mapping = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else "$"
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)

    return not stack


if __name__ == "__main__":
    assert valid_parantheses("")
    assert valid_parantheses("[][][]{}")
    assert valid_parantheses("(((){{}})())[]")
    assert not valid_parantheses("((((((())))))")

    print("Passed all tests!")
