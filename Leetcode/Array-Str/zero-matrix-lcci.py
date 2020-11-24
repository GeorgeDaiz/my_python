"""
零矩阵
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

示例 1：
输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

示例 2：
输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""


class Solution:
    @staticmethod
    def set_zeros(matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        has_zeros = 0
        for i in range(m):
            if matrix[i][0] == 0:
                has_zeros = 1
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if has_zeros:
                matrix[i][0] = 0


if __name__ == '__main__':
    ma = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    Solution().set_zeros(ma)
    print(ma)
