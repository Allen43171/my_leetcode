# 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums, k):
        # 當前總和=最大和=前k個元素的和
        curr_num = max_sum = sum(nums[:k])

        # 從第k個元素開始
        for i in range(k, len(nums)):
            # 更新當前總和，先減去窗口左邊的元素，再加上新的元素
            curr_num = curr_num - nums[i-k] + nums[i]
            
            # 更新最大和
            max_sum = max(max_sum, curr_num)

        # 返回最大平均值
        return max_sum / k
    
nums = [1,12,-5,-6,50,3]
k = 4
sol = Solution()

print("testcase1, ", nums)
testcase1 = sol.findMaxAverage(nums, k)
print(testcase1)

