# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        # 定義上下限
        max_limit = 2**31 - 1
        min_limit = -2**31

        # 初始化答案
        ans = 0

        # 判斷輸入正負
        if x >= 0:
            sign = 1
        else:
            sign = -1

        # 取絕對值
        x = abs(x)

        # 數字反轉
        while x > 0:
            ans = x % 10 + ans * 10  # 將 x 的最後一位加到 ans 的最前面
            x = int(x / 10)  # 移除 x 的最後一位

        # 乘以正負號
        ans = ans * sign

        # 檢查範圍，輸出成果
        if ans > max_limit or ans < min_limit:
            return 0
        else:
            return ans
