# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        # Remove spaces" " at the beginning and at the end of the string
        # " hello, world!   " >> "hello, world!"
        s = s.strip()
        list_s = list(s.split(" "))[::-1]
        ans = ""
        for i in range(len(list_s)):
            if list_s[i] != "":
                ans = ans + (list_s[i]) + " "

        return ans.rstrip()