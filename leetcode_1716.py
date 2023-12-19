# 1716. Calculate Money in Leetcode Bank
class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        n_7 = int(n//7)
        
        for i in range(n_7):
            ans = ans + 7*(i+4)
        # if n =  7, ans = 7*4
        # if n = 14, ans = 7*4 + 7*5
        # if n = 21, ans = 7*4 + 7*5 + 7*6
        
        if n%7 == 0:
            return ans
        else:
            for j in range(n_7+1, n_7+int(n%7)+1):
                ans = ans + j
            return (ans)