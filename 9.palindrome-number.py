#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            y = str(x)
            if y[::-1] == y:
                return True
        else:
            return False
 
# @lc code=end

