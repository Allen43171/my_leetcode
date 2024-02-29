# 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        the_numbers_of_zero = nums.count(0)

        while 0 in nums:
            nums.remove(0)

        for i in range(the_numbers_of_zero):
            nums.append(0)

        print(nums)