# 2652. Sum Multiples
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans_list = []
        for i in range(1, n+1):
            # print(i)
            if i%3 == 0:
                ans_list.append(i)
            elif i%5 == 0:
                ans_list.append(i)
            elif i%7 == 0:
                ans_list.append(i)
        return (sum(ans_list))
    
