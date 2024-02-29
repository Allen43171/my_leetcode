# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
# solution 1
class Solution_1:
    def minPartitions_1(self, n: str) -> int:
        s_list = [int(digit) for digit in n]
        count = 0
        while any(x > 0 for x in s_list):
            for i in range(len(s_list)):
                s_list[i] = max(0, s_list[i] - 1)
            count = count + 1
        return count
    
# solution 2
class Solution_2:
    def minPartitions_2(self, n: str) -> int:
        return (int(max(n)))