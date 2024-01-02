# 1910. Remove All Occurrences of a Substring
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans_judge = [""]
        for i in range(1, int(len(s))+1):
            
            # 只 replace 一次 
            s = s.replace(part, "",1)
            ans_judge.append(s)

            # To save time
            if ans_judge[i-1] == ans_judge[i]:
                break
        return (ans_judge[i])