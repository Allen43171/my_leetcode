# 2582. Pass the Pillow

# Input: n = 4, time = 5
# Output: 2
# 1 > 2 > 3 > 4 > 3 > 2
# 1234321 (1)234321 

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Generate people list
        people_list = [(i+1) for i in range(n)]

        # Generate repeat part
        # For example: (1)"23454321""23454321""23454321"...
        people_list_repeat = (people_list[1:] + people_list[::-1][1:])
        people_pass = people_list_repeat*time

        # Complete the order of passing pillow，12345432123454321...
        people_pass.insert(0, people_list[0])
        # print(people_pass)

        ans = people_pass[time]
        
        return ans
    