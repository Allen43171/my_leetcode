# 2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
            
        result = []
        s1 = set(nums1)
        s2 = set(nums2)
        result.append(list(s1 - s2))
        result.append(list(s2 - s1))

        return result