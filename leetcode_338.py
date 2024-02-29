# 338. Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        final_list = []
        for i in range(n+1):
            final_list.append(str(bin(i))[2:].count("1"))

        return (final_list)