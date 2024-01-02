# 1323. Maximum 69 Number

class Solution:
    def maximum69Number (self, num: int) -> int:
        n_list = list(str(num))
        for i in range(len(n_list)):
            if n_list[i] == "6":
                n_list[i] = "9"
                break

        return int("".join(n_list))
