#
# @lc app=leetcode id=2460 lang=python3
#
# [2460] Apply Operations to an Array
#

# @lc code=start
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0 
        zeros = nums.count(0)
        
        nums = [n for n in nums if n != 0]
        nums += [0]*zeros
        return nums
# @lc code=end

