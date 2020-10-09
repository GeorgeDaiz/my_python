# def queen(A, cur=0):
#     if cur == len(A):
#         print(A)
#         return 0
#     for col in range(len(A)):
#         A[cur], flag = col, True
#         for row in range(cur):
#             if A[row] == col or abs(col - A[row]) == cur - row:
#                 flag = False
#                 break
#         if flag:
#             queen(A, cur+1)
#
#
# queen([None]*8)


from typing import List
import collections


class Solution:
    def searchMatrix(self, matrix, target):
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


if __name__ == '__main__':
    ret = Solution().searchMatrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 19)
    print(ret)
