# 2710. Remove Trailing Zeros From a String
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return (num.replace("0", " ").rstrip().replace(" ", "0"))
        # return num.strip('0')
