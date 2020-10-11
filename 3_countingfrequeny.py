# Counting Frequency
"""
Given an unsorted list of some elements(may or may not be integers), Find the frequency of each
 distinct element in the list using a dictionary.
 Example:
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
Output :{ 1 : 5,2 : 4,3 : 3, 4 : 3, 5 : 2}

Explanation : Here 1 occurs 5 times, 2 occurs 4 times and so on...
"""

import unittest
def counting_frequency(lst):
    lst.sort()
    d1={}
    for i in lst:
        if (i not in d1):
            frequency=lst.count(i)
            d1[i]=frequency
    return d1


class TestCountingFrequency(unittest.TestCase):
    def test_1(self):
        lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
        d = {1: 5, 2: 4, 3: 3, 4: 3, 5: 2}
        self.assertEqual(counting_frequency(lst), d)

    def test_2(self):
        lst = ['a', 'b', 'c', 'a', 'b']
        d = {'a': 2, 'b': 2, 'c': 1}
        self.assertEqual(counting_frequency(lst), d)


if __name__ == '__main__':
    unittest.main(verbosity=2)
