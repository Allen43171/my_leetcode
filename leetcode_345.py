class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels =  "aeiouAEIOU"
        vowels_appear = []

        s_with_star = ""
        num_of_star = 0
        for char in s:
            if char in vowels:
                vowels_appear.append(char)
                s_with_star = s_with_star + "*"
                num_of_star = num_of_star + 1
            else:
                s_with_star = s_with_star + char

        vowels_appear = vowels_appear[::-1]

        s_final = ""
        vowel_index = 0

        for char in s_with_star:
            if char == "*":
                s_final = s_final + vowels_appear[vowel_index]
                vowel_index = vowel_index + 1
            else:
                s_final = s_final + char

        return (s_final)