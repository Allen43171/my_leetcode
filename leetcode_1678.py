# 1678. Goal Parser Interpretation
class Solution:
    def interpret(self, command: str) -> str:
        res = command.replace("()", "o").replace("(al)", "al")
        return res