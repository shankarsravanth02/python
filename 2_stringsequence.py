# String Sequence

"""
Given strings s0, s1 and a positive integer n, return the nth term of the sequence A where:
A[0] = s0
A[1] = s1
A[n] = A[n - 1] + A[n - 2] if n is even, otherwise A[n] = A[n - 2] + A[n - 1].
For example, given s0 = "a" and s1 = "b", the sequence A would be:
"a"
"b"
"ba" ("a" + "b")
"bba" ("b" + "ba")
"bbaba" ("bba" + "ba")

Example 1
Input
s0 = "et"
s1 = "r"
n = 0
Output
"et"

Example 2
Input
s0 = "a"
s1 = "p"
n = 1
Output
"p"

Example 3
Input
s0 = "zs"
s1 = "v"
n = 3
Output
"vvzs"

Example 4
Input
s0 = "dx"
s1 = "a"
n = 4
Output
"aadxadx"
"""

import unittest


def string_sequence(s0, s1, n):
    s3 = ""
    l1 = []
    l1.append(s0)
    l1.append(s1)
    for i in range(2, n+1, 1):
        if(i % 2 == 0):
            s3 = l1[i-1]+l1[i-2]
        else:
            s3 = l1[i-2]+l1[i-1]
        l1.append(s3)
    return l1[n]


string_sequence("et", "r", 0)


class TestStringSequence(unittest.TestCase):
    def test_1(self):
        self.assertEqual(string_sequence("et", "r", 0), "et")

    def test_2(self):
        self.assertEqual(string_sequence("a", "p", 1), "p")

    def test_3(self):
        self.assertEqual(string_sequence("zs", "v", 3), "vvzs")

    def test_4(self):
        self.assertEqual(string_sequence("dx", "a", 4), "aadxadx")


if __name__ == '__main__':
    unittest.main(verbosity=2)
