from typing import List

ones = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

ten = {
    "0": "Ten",
    "1": "Eleven",
    "2": "Twelve",
    "3": "Thirteen",
    "4": "Fourteen",
    "5": "Fifteen",
    "6": "Sixteen",
    "7": "Seventeen",
    "8": "Eighteen",
    "9": "Nineteen",
}

tens = {
    "2": "Twenty",
    "3": "Thirty",
    "4": "Forty",
    "5": "Fifty",
    "6": "Sixty",
    "7": "Seventy",
    "8": "Eighty",
    "9": "Ninety"
}

base = {
    1: "Thousand",
    2: "Million",
    3: "Billion"
}


def integer_to_english(num: int) -> str:
    """
    # 273: Convert a non-negative integer to its english words representation.

    Given input is guaranteed to be less than 231 - 1.
    """
    res = []

    # convert num to str to handle better
    s = str(num)

    # iterate in reverse order
    base_num = 0
    for i in range(1, len(s) + 1, 3):
        segment = s[-i:-i-3:-1]
        res = segment_to_english(segment, base_num) + res

        base_num += 1

    if not res:
        return "Zero"

    return " ".join(res)


def segment_to_english(segment: str, base_num: int) -> List["str"]:
    seg_res = []

    N = len(segment)
    for i in range(N - 1, -1, -1):
        num = segment[i]

        if num == "0":
            continue

        if i == 0:
            seg_res.append(ones[num])
        elif i == 1:
            if num == "1":
                seg_res.append(ten[segment[i-1]])
                break
            else:
                seg_res.append(tens[num])
        else:
            seg_res.append(ones[num])
            seg_res.append("Hundred")

    if seg_res and base_num in base:
        seg_res.append(base[base_num])

    return seg_res


if __name__ == "__main__":
    assert integer_to_english(123) == "One Hundred Twenty Three"
    assert integer_to_english(
        12345) == "Twelve Thousand Three Hundred Forty Five"
    assert integer_to_english(
        1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    assert integer_to_english(
        1234567891) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

    print("Passed all tests!")
