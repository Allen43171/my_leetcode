# 2418. Sort the People
# tuple
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined_names_heights = list(zip(names, heights))
        sorted_data = sorted(combined_names_heights, key=lambda x: (x[1], x[0]), reverse=True)
        sorted_names = [item[0] for item in sorted_data]

        return (list(sorted_names))

sol = Solution()

# testcase1
names = ["Mary","John","Emma"]
heights = [180,165,170]
testcase1 = sol.sortPeople(names, heights)
print(testcase1)

# testcase2
names = ["Alice","Bob","Bob"]
heights = [155,185,150]
testcase2 = sol.sortPeople(names, heights)
print(testcase2)