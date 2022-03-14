from unittest import TestCase
from math import ceil, sqrt


def construct_rectangle(area):
    first, second = None, None

    for i in range(int(ceil(sqrt(area))), 0, -1):
        if area % i == 0:
            return [i, area // i]

    return []


class Test(TestCase):
    def test_1(self):
        dimensions = construct_rectangle(4)
        self.assertEqual([2, 2], dimensions)

    def test_2(self):
        dimensions = construct_rectangle(37)
        self.assertIn(1, dimensions)
        self.assertIn(37, dimensions)

    def test_3(self):
        dimensions = construct_rectangle(122122)
        self.assertIn(427, dimensions)
        self.assertIn(286, dimensions)
