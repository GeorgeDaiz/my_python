"""
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

示例:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

说明:
给定矩阵中的元素总数不会超过 100000 。
"""
import collections


class Solution:
    @staticmethod
    def find_diagonal_order(matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        for k in range(m + n - 1):
            start = 0 if k < n else k + 1 - n
            end = m - 1 if k + 1 >= m else k
            if k % 2 == 0:
                for i in range(end, start - 1, -1):
                    res.append(matrix[i][k - i])
            else:
                for i in range(start, end + 1):
                    res.append(matrix[i][k - i])
        return res

    @staticmethod
    def find_diagonal_order1(matrix):
        if not matrix:
            return []
        dic = collections.defaultdict(list)
        res = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dic[i + j].append(matrix[i][j])
        for i in range(len(matrix) + len(matrix[0]) - 1):
            if i % 2 == 0:
                res += dic[i][::-1]
            else:
                res += dic[i]
        return res
