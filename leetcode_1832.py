# 1832. Check if the Sentence Is Pangram
from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(Counter(sentence)) == 26:
            return True
        else:
            return False