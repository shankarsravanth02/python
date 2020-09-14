import unittest
from itertools import permutations

question_04 = """
Rotating primes

Given an integer n, return whether every rotation of n is prime.
Example 1:
Input:
n = 199
Output:
True
Explanation:
199 is prime, 919 is prime, and 991 is prime.

Example 2:
Input:
n = 19
Output:
False
Explanation:
Although 19 is prime, 91 is not.
"""


# Implement the below function and run the program

def is_rotating_prime(num):
    changes=permutations(str(num))
    list1=[]
    count=0
    for i in list(changes):
        strings="".join(i)
        list1.append(int(strings))
    for k in list1:
        if (k>1):
            for j in range(2,k):
                if (k%j==0):
                    break
            else:
                count=count+1
    if (count==len(list1)):
        return True
    else: return False


class TestIsRotatingPrime(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_rotating_prime(2), True)

    def test_2(self):
        self.assertEqual(is_rotating_prime(199), True)

    def test_3(self):
        self.assertEqual(is_rotating_prime(19), False)

    def test_4(self):
        self.assertEqual(is_rotating_prime(791), False)

    def test_5(self):
        self.assertEqual(is_rotating_prime(919), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
