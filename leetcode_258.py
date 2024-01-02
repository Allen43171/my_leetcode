# 258. Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            while num > 9:
                answer = 0
                while num:
                    answer = answer + num%10
                    num = num//10
                num = answer
            return (answer)
