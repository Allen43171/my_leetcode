# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        while i < 10000:
            s = s.replace("[]", "")
            s = s.replace("()", "")
            s = s.replace("{}", "")
            i+=1
            if s == "":
                break

        if s == "":
            return True
        else:
            return False

