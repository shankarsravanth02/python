# Pig Latin

"""
Given a string s, return a new string where for every word the first character
is moved the end with the suffix "ay" added.

Example 1
Input

s = "hello world"
Output

"ellohay orldway"
"""

import unittest


def pig_latin(s):
    to_list=s.split(" ")
    result=[]
    for i in to_list:
        r=i+i[0]+"ay"
        result.append(str(r[1:]))
    return " ".join(result)


# DO NOT TOUCH THE BELOW CODE


class TestPigLatin(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pig_latin(
            "hello world"), "ellohay orldway")

    def test_2(self):
        self.assertEqual(pig_latin(
            "welcom to python"), "elcomway otay ythonpay")


if __name__ == '__main__':
    unittest.main(verbosity=2)
