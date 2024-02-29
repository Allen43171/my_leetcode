# 1281. Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ans = 0
        product_of_digits = 1
        sum_of_digits = 0

        while n>0:
            ans = n%10
            product_of_digits *= ans
            sum_of_digits += ans
            n = int(n/10)

        ans = product_of_digits-sum_of_digits

        return ans

# Test
# my_solution = Solution()
# print("Please type any number")
# testcase = int(input())
# use_method = my_solution.subtractProductAndSum(n = testcase)
# print(use_method)
