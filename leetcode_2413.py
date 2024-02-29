# 2413. Smallest Even Multiple

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 == 0:
            return n
        elif n%2 == 1:
            return 2*n