# 2011. Final Value of Variable After Performing Operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num_list = []
        for i in operations:
            if i == "--X" or i == "X--":
                num_list.append(-1)
            elif i == "++X" or i == "X++":
                num_list.append(1)
                
        ans = sum(num_list)
        return (ans)