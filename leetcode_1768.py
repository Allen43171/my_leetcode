# 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        max_len = max(len1, len2)

        word1 = word1.ljust(max_len)
        word2 = word2.ljust(max_len)

        merged_list = []
        for char1, char2 in zip(word1, word2):
            merged_list.append(char1+char2)

        return ("".join(merged_list).replace(" ", ""))


