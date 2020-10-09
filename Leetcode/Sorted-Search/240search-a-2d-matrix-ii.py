"""
240.搜索二维矩阵II
编写一个高效的算法来搜索mxn矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例:
现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target=5，返回true。

给定target=20，返回false。
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix, target):
        # 二分法
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical = self.binary_search(matrix, target, i, True)
            horizontal = self.binary_search(matrix, target, i, False)
            if vertical or horizontal:
                return True

        return False

    def binary_search(self, matrix, target, start, flag):
        lo = start
        hi = len(matrix[0]) - 1 if flag else len(matrix) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            # search a column
            if flag:
                if matrix[start][mid] > target:
                    hi = mid - 1
                elif matrix[start][mid] < target:
                    lo = mid + 1
                else:
                    return True
            else:
                if matrix[mid][start] > target:
                    hi = mid - 1
                elif matrix[mid][start] < target:
                    lo = mid + 1
                else:
                    return True
        return False

    def searchMatrix1(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        height = len(matrix)
        width = len(matrix[0])

        row = height - 1
        col = 0
        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False
