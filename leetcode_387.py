# 387. First Unique Character in a String
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = dict(Counter(list(s)))
        s_dict_keys = list(s_dict.keys())
        s_dict_values = list(s_dict.values())

        final_ans = 0
        for i in range(len(s_dict_values )):
            if s_dict_values[i] == 1:
                final_ans = list(s).index(s_dict_keys[i])
                break
            else:
                final_ans = -1
        
        return (final_ans)
    
# test
sol = Solution()
testcase1 = sol.firstUniqChar("leetcode")
print(testcase1)

