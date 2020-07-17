from typing import Any, List, Tuple


def reorder_log_files(logs: List[str]) -> List[str]:
    """
    # 937: You have an array of logs.  Each log is a space delimited string of words.

    For each log, the first word in each log is an alphanumeric identifier.  Then, either:
        = Each word after the identifier will consist only of lowercase letters, or;
        - Each word after the identifier will consist only of digits.
        - We will call these two varieties of logs letter-logs and digit-logs. 
        - It is guaranteed that each log has at least one word after its identifier.

    Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are 
    ordered lexicographically ignoring identifier, with the identifier used in case of ties.
    The digit-logs should be put in their original order.

    Return the final order of the logs.
    """
    def f(log: List[str]) -> Tuple[Any]:
        _id, rest = log.split(" ", 1)
        return (0, rest, _id) if rest[0].isalpha() else (1,)

    return list(sorted(logs, key=f))


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
            "let2 own kit dig", "let3 art zero"]
    expected = ["let1 art can", "let3 art zero",
                "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
    assert reorder_log_files(logs) == expected

    logs = ["5 m w", "j mo", "t q h", "g 07", "o 2 0"]
    expected = ["5 m w", "j mo", "t q h", "g 07", "o 2 0"]
    assert reorder_log_files(logs) == expected

    print("Passed all tests!")
