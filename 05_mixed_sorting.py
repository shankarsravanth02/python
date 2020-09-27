# Mixed sorting

"""
Given a list of integers nums, sort the array such that:

All even numbers are sorted in increasing order
All odd numbers are sorted in decreasing order
The relative positions of the even and odd numbers remain the same
Example 1
Input

nums = [8, 13, 11, 90, -5, 4]
Output

[4, 13, 11, 8, -5, 90]
Explanation

The even numbers are sorted in increasing order, the odd numbers are sorted in 
decreasing number, and the relative positions were 
[even, odd, odd, even, odd, even] and remain the same after sorting.
"""

# solution

import unittest


def mixed_sorting(nums):
    location=[]
    evens=[]
    odds=[]
    total=[]
    x=y=0
    for i in nums:
        if(i%2==0):
            location.append(1)
            evens.append(i)
        elif(i%2==1):
            location.append(0)
            odds.append(i)
    m=sorted(evens)
    n=sorted(odds)
    k=n[::-1]
    for c in location:
        if (c==1):
            total.append(m[x])
            x=x+1
        else:
            total.append(k[y])
            y=y+1
        return total


# DO NOT TOUCH THE BELOW CODE


class TestMixedSorting(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mixed_sorting(
            [8, 13, 11, 90, -5, 4]), [4, 13, 11, 8, -5, 90])

    def test_2(self):
        self.assertEqual(mixed_sorting([1, 2, 3, 6, 5, 4]), [5, 2, 3, 4, 1, 6])


if __name__ == '__main__':
    unittest.main(verbosity=2)
