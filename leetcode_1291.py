# 1291. Sequential Digits
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digit_one_to_nine = "123456789"
        ans_list = []

        # 迴圈從 low 所在的位數到 high 所在的位數
        for i in range(len(str(low)), len(str(high))+1):
            # 在 0 到 10-i 之間
            for j in range(10-i):
                ans_number = int(digit_one_to_nine[j:j+i])
                # 檢查是否在指定範圍內
                if ans_number >= low and ans_number <= high:
                    # 將符合條件的數字添加到結果列表中
                    ans_list.append(int(digit_one_to_nine[j:j+i]))
        
        return ans_list