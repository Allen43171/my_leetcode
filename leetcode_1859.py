# 1859. Sorting the Sentence
class Solution:
    def sortSentence(self, s: str) -> str:
        res = " "
        s_without_space = len(s) - len(s.replace(" ", "")) + 1
        for i in range(1, s_without_space+1):
            if str(i) in s:
                res += str((s.replace(s[s.index(str(i)):], "")).split(" ")[-1]) + " "

        return res.strip()
