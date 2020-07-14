def angle_clock(hour: int, minutes: int) -> int:
    """
    # 1344: Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between 
    the hour and the minute hand.
    """
    hr_angle = (30 * hour) + (0.5 * minutes)
    mins_angle = 6 * minutes

    a = abs(hr_angle - mins_angle)
    return a if a <= 180 else 360 - a


if __name__ == "__main__":
    assert angle_clock(12, 30) == 165.0
    assert angle_clock(3, 15) == 7.5
    assert angle_clock(4, 50) == 155.0
    assert angle_clock(12, 0) == 0.0

    print("Passed all tests!")