def num_water_bottles(num_bottles: int, num_exchange: int) -> int:
    """
    # 1518: Given numBottles full water bottles, you can exchange numExchange empty water bottles for 
    one full water bottle.

    The operation of drinking a full water bottle turns it into an empty bottle.

    Return the maximum number of water bottles you can drink.
    """
    ans = num_bottles
    while num_bottles >= num_exchange:
        x, y = divmod(num_bottles, num_exchange)
        ans += x
        num_bottles = x + y

    return ans


if __name__ == "__main__":
    assert num_water_bottles(9, 3) == 13
    assert num_water_bottles(15, 4) == 19
    assert num_water_bottles(5, 5) == 6
    assert num_water_bottles(2, 3) == 2

    print("Passed all tests!")
