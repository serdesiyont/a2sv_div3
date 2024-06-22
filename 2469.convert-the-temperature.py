#
# @lc app=leetcode id=2469 lang=python3
#
# [2469] Convert the Temperature
#

# @lc code=start
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        output = []

        kelvin = 273.15 + celsius
        fahrenheit = 9/5 * celsius + 32

        output.append(kelvin)
        output.append(fahrenheit)
        return output
        
# @lc code=end

