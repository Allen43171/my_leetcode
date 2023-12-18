#　1464. Maximum Product of Two Elements in an Array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        return ((nums[0]-1)*(nums[1]-1))