# 58. Length of Last Word
# Solution 1
# for loop
class Solution_1:
    def lengthOfLastWord_1(self, s: str) -> int:
        
        state_list = []
        for i in range(len(s)):
            if s[::-1][i] == " ":
                state_list.append("X")
            else:
                state_list.append("O")
            if state_list[i-1] == "O" and state_list[i] == "X":
                break

        return (state_list.count("O"))
    
# Solution 2
# .strip()
class Solution_2:
    def lengthOfLastWord_2(self, s: str) -> int:
        s = s.strip(' ')
        s_list = s.split(" ")
        
        return (len(s_list[-1]))
