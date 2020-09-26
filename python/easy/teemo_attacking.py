from typing import List


def find_poisoned_duration(time_series: List[int], duration: int) -> int:
    """
    # 495: In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe 
    be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe 
    and the poisoning time duration per Teemo's attacking, you need to output the total time that 
    Ashe is in poisoned condition.

    You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe 
    be in poisoned condition immediately.
    """
    if not time_series:
        return 0

    N, total_time = len(time_series), 0
    for i in range(N - 1):
        diff = time_series[i + 1] - time_series[i]
        total_time += duration if diff >= duration else diff

    return total_time + duration


if __name__ == "__main__":
    time_series = [1, 4]
    assert find_poisoned_duration(time_series, 2) == 4

    time_series = [1, 2]
    assert find_poisoned_duration(time_series, 2) == 3

    print("Passed all tests!")
