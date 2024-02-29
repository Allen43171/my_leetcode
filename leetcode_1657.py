# 1657. Determine if Two Strings Are Close

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        list_1 = dict( Counter(list(word1)) )
        list_2 = dict( Counter(list(word2)) )

        values_1 = [i for i in list_1.values()]
        keys_1 = [i for i in list_1.keys()]
        values_2 = [i for i in list_2.values()]
        keys_2 = [i for i in list_2.keys()]

        keys_1 = sorted(keys_1)
        keys_2 = sorted(keys_2)

        if sorted(values_1) == sorted(values_2) and keys_1 == keys_2:
            return True
        else:
            return False

# test case
word1 = "abc"
word2 = "bcu"
solution = Solution()
print(solution.closeStrings(word1, word2))