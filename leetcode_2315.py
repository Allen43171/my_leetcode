# 2315. Count Asterisks
class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "|":
                count += 1
            if count%2 == 0:
                if s[i]=="*":
                    res = res + 1

        return res