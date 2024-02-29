# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans_tem = 0
        for i in range(len(digits)):
            ans_tem = ans_tem + (digits[len(digits)-i-1]*(10**i))
        ans_tem = ans_tem + 1

        ans = []
        while ans_tem>0:
            ans.append(ans_tem%10)
            ans_tem = ans_tem//10
            
        return ans[::-1]