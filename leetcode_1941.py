# 1941. Check if All Characters Have Equal Number of Occurrences
from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter_time = list(Counter(s).values())
        for i in range(1, len(counter_time)):
            if counter_time[i-1] != counter_time[i]:
                return False
        return True