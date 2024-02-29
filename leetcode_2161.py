# 2161. Partition Array According to Given Pivot
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # create 3 empty list
        res_less = []
        res_equal = []
        res_more = []

        # for loop to put element in those lists
        for ele in nums:
            if ele < pivot:
                res_less.append(ele)
            elif ele > pivot:
                res_more.append(ele)
            elif ele == pivot:
                res_equal.append(ele)
        res = res_less + res_equal + res_more

        return res
    