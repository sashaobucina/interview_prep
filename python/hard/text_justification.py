from typing import List


def full_justify(words: List[str], max_width: int) -> List[str]:
    """
    # 68: Given an array of words and a width maxWidth, format the text such that each line has exactly 
    maxWidth characters and is fully (left and right) justified.

    You should pack your words in a greedy approach; that is, pack as many words as you can 
    in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. If the number of spaces 
    on a line do not divide evenly between words, the empty slots on the left will be assigned more 
    spaces than the slots on the right.

    For the last line of text, it should be left justified and no extra space is inserted between words.

    NOTE:
        - A word is defined as a character sequence consisting of non-space characters only.
        - Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
        - The input array words contains at least one word.
    """
    res = []

    curr_len = -1
    i, j = 0, 0

    while j < len(words) - 1:
        curr_len += len(words[j]) + 1

        if curr_len + len(words[j+1]) < max_width:
            j += 1
        else:
            line = words[i:j+1]

            if len(line) == 1:
                res.append(ljust(line, max_width))
            else:
                mid = construct(line[1:-1], max_width -
                                len(line[0]) - len(line[-1]))
                res.append(line[0] + mid + line[-1])

            j += 1
            i = j
            curr_len = -1

    # add final line
    res.append(ljust(words[i:], max_width))

    return res


def construct(line: List[str], width: int) -> str:
    res = ""
    spaces = sum([len(word) for word in line])
    space, mod = divmod(width - spaces, len(line) + 1)

    for i in range(len(line)):
        res += " " * (space + int(mod > 0)) + line[i]
        mod -= 1

    return res + (" " * space)


def ljust(line: List[str], max_width: int) -> str:
    content = " ".join(line)
    whitespace = " " * (max_width - len(content))

    return content + whitespace


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    expected = ["This    is    an", "example  of text", "justification.  "]
    assert full_justify(words, 16) == expected

    print("Passed all tests!")
