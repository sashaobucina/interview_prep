class Logger:
    """
    # 359: Design a logger system that receive stream of messages along with its timestamps, each message 
    should be printed if and only if it is not printed in the last 10 seconds.

    Given a message and a timestamp (in seconds granularity), return true if the message should be printed 
    in the given timestamp, otherwise returns false.

    It is possible that several messages arrive roughly at the same time.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.time_map:
            self.time_map[message] = timestamp
            return True

        if (timestamp - self.time_map[message]) >= 10:
            self.time_map[message] = timestamp
            return True

        return False


if __name__ == "__main__":
    logger = Logger()
    assert logger.shouldPrintMessage(1, "foo")
    assert logger.shouldPrintMessage(2, "bar")
    assert not logger.shouldPrintMessage(3, "foo")
    assert not logger.shouldPrintMessage(8, "bar")
    assert not logger.shouldPrintMessage(10, "foo")
    assert logger.shouldPrintMessage(11, "foo")

    print("Passed all tests!")
