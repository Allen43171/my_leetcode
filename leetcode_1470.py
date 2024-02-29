# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums_x = nums[0:n]
        nums_y = nums[n:]
        nums_shuffle = []
        for i in range(n):
            nums_shuffle.append(nums_x[i])
            nums_shuffle.append(nums_y[i])
        
        return (nums_shuffle)

