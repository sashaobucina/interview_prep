from typing import List


def validate_utf_8(data: List[int]) -> bool:
    """
    # 393: A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
    - for 1-byte character, the first bit is a 0, followed by its unicode code.
    - for n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes 
        with most significant 2 bits being 10.

    Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

    NOTE: The input is an array of integers. Only the least significant 8 bits of each integer is 
    used to store the data. This means each integer represents only 1 byte of data.
    """
    n_bytes = 0
    for num in data:
        byte = int_to_byte(num)

        if n_bytes == 0:
            for bit in byte:
                if bit == "0":
                    break
                n_bytes += 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if byte[:2] != "10":
                return False

        n_bytes -= 1

    return n_bytes == 0


def validate_utf_8_mask(data: List[int]) -> bool:
    """
    # 393: Solving same problem but now using bit manipulation.
    """
    n_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6
    for num in data:
        if n_bytes == 0:
            mask = 1 << 7

            while mask & num:
                n_bytes += 1
                mask >>= 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0


def int_to_byte(x: int) -> str:
    """ Return the byte representation (base 2) of an integer. """
    return "{0:08b}".format(x)


if __name__ == "__main__":
    data = [25]
    assert validate_utf_8(data)
    assert validate_utf_8_mask(data)

    data = [197, 130, 1]
    assert validate_utf_8(data)
    assert validate_utf_8_mask(data)

    data = [235, 140, 4]
    assert not validate_utf_8(data)
    assert not validate_utf_8_mask(data)

    print("Passed all tests!")
