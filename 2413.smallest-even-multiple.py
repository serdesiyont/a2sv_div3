#
# @lc app=leetcode id=2413 lang=python3
#
# [2413] Smallest Even Multiple
#

# @lc code=start
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 != 0:
            return 2*n
        else:
            return n
# @lc code=end

