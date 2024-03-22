# 2000. Reverse Prefix of Word
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            word_index = word.index(ch)
            return (word[0:word_index+1][::-1] + word[word_index+1:])
        else:
            return (word)