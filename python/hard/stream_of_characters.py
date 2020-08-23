from typing import List
from collections import deque


class StreamChecker:
    """
    # 1032: Implement the StreamChecker class as follows:

        - StreamChecker(words): Constructor, init the data structure with the given words.
        - query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order 
            from oldest to newest, including this letter just queried) spell one of the words in the 
            given list.
    """

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]

            node["$"] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        node = self.trie
        for ch in self.stream:
            if "$" in node:
                return True
            if not ch in node:
                return False

            node = node[ch]

        return "$" in node


if __name__ == "__main__":
    stream_checker = StreamChecker(["cd", "f", "kl"])
    assert not stream_checker.query("a")
    assert not stream_checker.query("b")
    assert not stream_checker.query("c")
    assert stream_checker.query("d")
    assert not stream_checker.query("e")
    assert stream_checker.query("f")
    assert not stream_checker.query("g")
    assert not stream_checker.query("h")
    assert not stream_checker.query("i")
    assert not stream_checker.query("j")
    assert not stream_checker.query("k")
    assert stream_checker.query("l")

    print("Passed all tests!")
