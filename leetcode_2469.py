# 2469. Convert the Temperature

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # Kelvin = Celsius + 273.15
        # Fahrenheit = Celsius * 1.80 + 32.00
        k = celsius +273.15
        f = celsius * 1.80 +32.00
        
        # The request is to retain up to 5 decimal places, 
        # although the question does not seem to explicitly require it. 
        # However, when executed on the LeetCode website, 
        # the result appears to preserve up to 5 decimal places.
        ans = [float('%.5f'%k), float("%.5f"%f)]

        return ans