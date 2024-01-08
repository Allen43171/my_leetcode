# 2023. Number of Pairs of Strings With Concatenation Equal to Target

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    pass
                else:
                    num_target_or_not = (nums[i]+nums[j])
                    if num_target_or_not == target:
                        count += 1
                    else:
                        pass

        return (count)