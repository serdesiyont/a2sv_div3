#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        transpose_mat = [[matrix[j][i] for j in range(r)] for i in range(c)]
        # lis = []
        # for i in range(c):
        #     for j in range(r):
        #         lis.append(matrix[j][i])
        #     transpose_mat.append(list(lis))
        #     lis.clear()
        return transpose_mat
# @lc code=end

