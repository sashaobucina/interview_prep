from collections import deque


class HitCounter:
    """
    # 362: Design a hit counter which counts the number of hits received in the past 5 minutes.

    Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls
    are being made to the system in chronological order (ie, the timestamp is monotonically increasing). 
    You may assume that the earliest timestamp starts at 1.

    It is possible that several hits arrive roughly at the same time.
    """

    def __init__(self):
        self.hits = deque([])

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while len(self.hits) and (timestamp - self.hits[0]) >= 300:
            self.hits.popleft()
        self.hits.append(timestamp)

    def get_hits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while len(self.hits) and (timestamp - self.hits[0]) >= 300:
            self.hits.popleft()
        return len(self.hits)


if __name__ == "__main__":
    hit_counter = HitCounter()
    hit_counter.hit(1)
    hit_counter.hit(2)
    hit_counter.hit(3)
    assert hit_counter.get_hits(4) == 3
    hit_counter.hit(300)
    assert hit_counter.get_hits(300) == 4
    assert hit_counter.get_hits(301) == 3

    print("Passed all tests!")
