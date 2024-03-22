# 3019. Number of Changing Keys
class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.upper()
        count = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                count += 1

        return (count)