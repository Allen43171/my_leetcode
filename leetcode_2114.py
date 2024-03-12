# 2114. Maximum Number of Words Found in Sentences
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        num_of_word = 0
        for sentence in sentences:
            sentence_len = len(sentence)
            sentence_len_without_space = len(sentence.replace(" ", ""))
            num_of_word = max(sentence_len - sentence_len_without_space + 1, num_of_word)
        
        return (num_of_word)