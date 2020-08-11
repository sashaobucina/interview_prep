from collections import defaultdict


class TimeMap:
    """
    # 981: Create a timebased key-value store class TimeMap, that supports two operations.

    1. set(string key, string value, int timestamp)
        - Stores the key and value, along with the given timestamp.

    2. get(string key, int timestamp)
        - Returns a value such that set(key, value, timestamp_prev) was called previously, w/ timestamp_prev <= timestamp.
        - If there are multiple such values, it returns the one with the largest timestamp_prev.
        - If there are no values, it returns the empty string ("").
    """

    def __init__(self):
        self.items = defaultdict(list)
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.items[key].append(value)
        self.times[(key, value)] = timestamp

    def get(self, key: str, timestamp: int) -> str:
        values = self.items[key]

        for i in range(len(values) - 1, -1, -1):
            if self.times[(key, values[i])] <= timestamp:
                return values[i]

        return ""


if __name__ == "__main__":
    # Test set #1
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 3) == "bar"
    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"

    # Test set #2
    time_map = TimeMap()
    time_map.set("love", "high", 10)
    time_map.set("love", "low", 20)
    assert time_map.get("love", 5) == ""
    assert time_map.get("love", 10) == "high"
    assert time_map.get("love", 15) == "high"
    assert time_map.get("love", 20) == "low"
    assert time_map.get("love", 25) == "low"

    print("Passed all tests!")
