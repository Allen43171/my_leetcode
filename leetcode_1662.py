# 1662. Check If Two String Arrays are Equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        s2 = ""

        for i in word1:
            s1 = s1 + i
        for i in word2:
            s2 = s2 + i
            
        if s1 == s2:
            return True
        elif s1 != s2:
            return False