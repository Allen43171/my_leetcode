# 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        t_list = [0,1,1]
        for i in range(len(t_list)+n-2-3):
            t_list.append(t_list[i] + t_list[i+1] + t_list[i+2])

        return (t_list[n])

# test case

n = 5
solution = Solution()
print(solution.tribonacci(n))