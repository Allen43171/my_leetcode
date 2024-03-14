# 2810. Faulty Keyboard
class Solution:
    def finalString(self, s: str) -> str:
        res = ""
        for le in s:
            res += le
            if le == "i":
                res = res[::-1].replace("i", "")

        return (res)