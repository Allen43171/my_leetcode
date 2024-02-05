# 387. First Unique Character in a String
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 使用 Counter 統計每個字符的出現次數
        s_dict = dict(Counter(list(s)))

        # 取得鍵、值
        s_dict_keys = list(s_dict.keys())
        s_dict_values = list(s_dict.values())

        final_ans = 0
        for i in range(len(s_dict_values )):
            # 如果出現次數為 1，表示是第一個不重複的字
            if s_dict_values[i] == 1:
                # 找到該字符在原始字符串中的索引
                final_ans = list(s).index(s_dict_keys[i])
                break
            else:
                # 如果不存在不重複的字符，將結果設為 -1
                final_ans = -1
        
        return (final_ans)
    
# test
sol = Solution()
testcase1 = sol.firstUniqChar("leetcode")
print(testcase1)

