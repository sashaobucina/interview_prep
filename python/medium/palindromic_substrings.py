from unittest import TestCase


def count_substrings(s):
    count = 0

    for idx, ch in enumerate(s):
        count += _palindromic_substring_count(s, idx, idx)
        count += _palindromic_substring_count(s, idx, idx + 1)

    return count


def _palindromic_substring_count(s, start, end):
    count = 0

    while start >= 0 and end < len(s):
        if s[start] != s[end]:
            break

        count += 1
        start -= 1
        end += 1

    return count


class Test(TestCase):
    def test_1(self):
        self.assertEqual(3, count_substrings("abc"))

    def test_2(self):
        self.assertEqual(6, count_substrings("aaa"))

    def test_3(self):
        self.assertEqual(10, count_substrings("racecar"))
