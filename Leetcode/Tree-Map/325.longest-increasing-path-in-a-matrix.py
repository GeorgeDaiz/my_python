"""
329.矩阵中的最长递增路径
给定一个m x n 整数矩阵matrix ，找出其中 最长递增路径 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。

示例 1：
输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4 
解释：最长递增路径为[1, 2, 6, 9]。

示例 2：
输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4 
解释：最长递增路径是[3, 4, 5, 6]。注意不允许在对角线方向上移动。

示例 3：
输入：matrix = [[1]]
输出：1

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""
from typing import List
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        rows, columns = len(matrix), len(matrix[0])

        @lru_cache
        def dfs(row, column):
            best = 1
            for dx, dy in dirs:
                new_row, new_col = row + dx, column + dy
                if 0 <= new_row < rows and 0 <= new_col < columns and matrix[new_row][new_col] > matrix[row][column]:
                    best = max(best, dfs(new_row, new_col) + 1)
            return best

        res = 0
        for i in range(rows):
            for j in range(columns):
                res = max(res, dfs(i, j))
        return res

