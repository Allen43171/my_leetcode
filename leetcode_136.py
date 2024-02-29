# 136. Single Number

# method 1, for-loop
class Solution_1:
    def singleNumber(self, nums: List[int]) -> int:
        for ele in nums:
            if (nums.count(ele)) == 1:
                return (ele)

# method 2, dictionary 
class Solution_2:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict.pop(i)
        return int(*dict)