#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return True
        else:
            for i in range(len(matrix)-1):
                for j in range(len(matrix[i])-1):
                    if matrix[i][j] != matrix[i+1][j+1]:
                        return False 
                        
            return True

                
        
# @lc code=end

