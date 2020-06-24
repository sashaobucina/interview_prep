def armstrong_number(num: int) -> bool:
    """
    # 1134: A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.
    """
    tmp = num
    summed = 0
    while tmp > 0:
        digit = tmp % 10
        summed += digit ** 3
        tmp //= 10

    return summed == num


if __name__ == "__main__":
    armstong_numbers = [0, 1, 153, 370, 407]
    for num in armstong_numbers:
        assert armstrong_number(num)

    non_armstrong_numbers = [2, 8, 154, 372, 408]
    for num in non_armstrong_numbers:
        assert not armstrong_number(num)

    print("Passed all tests!")
