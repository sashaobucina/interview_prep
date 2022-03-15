from unittest import TestCase


def read_binary_watch(turned_on):
    """
    A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

    Given an integer turnedOn which represents the number of LEDs that are currently on, return all possible times the watch could represent. You may return the answer in any order.

    The hour must not contain a leading zero.

    For example, "01:00" is not valid. It should be "1:00".
    The minute must be consist of two digits and may contain a leading zero.

    For example, "10:2" is not valid. It should be "10:02".
    """
    res = []

    for i in range(12):
        for j in range(60):
            if (bin(i) + bin(j)).count("1") == turned_on:
                res.append("%s:%s" % (str(i), str(j).zfill(2)))

    return res


class Test(TestCase):
    def test_1(self):
        times = read_binary_watch(1)

        self.assertIn("0:01", times)
        self.assertIn("0:02", times)
        self.assertIn("0:04", times)
        self.assertIn("0:08", times)
        self.assertIn("0:16", times)
        self.assertIn("0:32", times)
        self.assertIn("1:00", times)
        self.assertIn("2:00", times)
        self.assertIn("4:00", times)
        self.assertIn("8:00", times)

    def test_2(self):
        times = read_binary_watch(9)

        self.assertEquals([], times)
