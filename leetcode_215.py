# 215. Kth Largest Element in an Array

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.nlargest，用heapq取出最大的前幾個元素
        return (heapq.nlargest(k, nums)[k-1])
