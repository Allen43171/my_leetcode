# 1512. Number of Good Pairs
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_list = (list(Counter(nums).values()))
        res = 0
        for i in nums_list:
            res += (i*(i-1))//2

        return res