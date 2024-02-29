# 2299. Strong Password Checker II
# String processing
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # 至少8碼
        def is_string_length_over_eight(password):
            if len(password) >= 8:
                return True
            else:
                return False

        # 至少一個小寫
        def is_string_contain_lower(password):
            for char in password:
                if char.islower():
                    return True
            return False

        # 至少一個大寫
        def is_string_contain_upper(password):
            for char in password:
                if char.isupper():
                    return True
            return False

        # 至少一個數字
        def is_string_contain_digit(password):
            digit_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for i in digit_list:
                if i in password:
                    return True
            return False

        # 至少一個特殊符號，"!@#$%^&*()-+"
        def is_string_contain_special_characters(password):
            special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]
            for i in special_characters:
                if i in password:
                    return True
            return False

        # 不能有連續兩碼一樣
        def not_contain_two_same_characters(password):
            for i in range(1, len(password)):
                if password[i-1] == password[i]:
                    return False
            return True

        ans = is_string_length_over_eight(password) and \
            is_string_contain_lower(password) and \
            is_string_contain_upper(password) and \
            is_string_contain_digit(password) and \
            is_string_contain_special_characters(password) and \
            not_contain_two_same_characters(password)
        
        return ans

# Test case
# password = password = "1aB!"
# password = "IloveLe3tcode!"`

# code check
# print("---"*30)
# print(is_string_length_over_eight(password))
# print(is_string_contain_lower(password))
# print(is_string_contain_upper(password)) 
# print(is_string_contain_digit(password))
# print(is_string_contain_special_characters(password)) 
# print(not_contain_two_same_characters(password))