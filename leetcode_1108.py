# 1108. Defanging an IP Address
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # repplace "." with "[.]"
        ans = address.replace(".", "[.]")
        return ans