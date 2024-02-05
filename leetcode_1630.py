# 1630. Arithmetic Subarrays
class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        ans_boolean = []
        tem_list = []
        for i in range(len(r)):
            # 將範圍l[i] 到 r[i]的數字新增到tem_list
            tem_list.append(nums[l[i]:r[i]+1])
            sorted_list = sorted(tem_list[i])
            
            # 確定公差及狀態
            common_difference = sorted_list[1] - sorted_list[0]
            ans_state = 0
            for j in range(1, len(sorted_list)):
                # 非等差，將狀態設定為1
                if sorted_list[j]-sorted_list[j-1] != common_difference:
                    ans_state = 1

            if ans_state == 0:
                ans_boolean.append(True)
            else:
                ans_boolean.append(False)

        return ans_boolean

# testcase
nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]

sol = Solution()
testcase = sol.checkArithmeticSubarrays(nums, l, r)
print(testcase)