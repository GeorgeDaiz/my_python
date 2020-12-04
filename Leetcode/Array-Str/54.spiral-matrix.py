"""
54.螺旋矩阵
给定一个包含m x n个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List


class Solution:
    # 暴力模拟
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[0] * n for _ in range(m)]
        ans = [0] * (m * n)

        row, column = 0, 0
        dir_idx = 0
        for i in range(m * n):
            ans[i] = matrix[row][column]
            visited[row][column] = 1
            next_row, next_col = row + dirs[dir_idx][0], column + dirs[dir_idx][1]
            if not(0 <= next_row < m and 0 <= next_col < n and not visited[next_row][next_col]):
                dir_idx = (dir_idx + 1) % 4

            row += dirs[dir_idx][0]
            column += dirs[dir_idx][1]

        return ans

    # 按层模拟
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        ans = []
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            for column in range(left, right+1):
                ans.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                ans.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    ans.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    ans.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return ans


if __name__ == '__main__':
    ret = Solution().spiralOrder1([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    print(ret)
