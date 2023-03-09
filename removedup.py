from typing import Counter


def removedup(nums):
    count=0
    for i in nums:
        if Counter(i)>0:
            count=count+1
            

