# 1207. Unique Number of Occurrences

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        my_dict = dict(Counter(arr))
        values = [i for i in my_dict.values()]

        if len(values) == len(set(values)):
            return (True)
        else:
            return (False)

# 測試
arr =  [1,2]
solution = Solution()
print(solution.uniqueOccurrences(arr))
