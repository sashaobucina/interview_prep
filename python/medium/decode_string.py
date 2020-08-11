def decode_string(s: str) -> str:
    """
    # 394: The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
    is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

    You may assume that the input string is always valid; No extra white spaces, square brackets are 
    well-formed, etc.

    Furthermore, you may assume that the original data does not contain any digits and that digits 
    are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
    """
    stk = []
    curr_num, curr_str = 0, ""

    for ch in s:
        if ch == "[":
            stk.append((curr_num, curr_str))
            curr_num, curr_str = 0, ""
        elif ch == "]":
            num, prev_str = stk.pop()
            curr_str = prev_str + (num * curr_str)
        elif ch.isdigit():
            curr_num *= 10
            curr_num += int(ch)
        else:
            curr_str += ch

    return curr_str


if __name__ == "__main__":
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert decode_string("abc3[cd]xyz") == "abccdcdcdxyz"

    print("Passed all tests!")
