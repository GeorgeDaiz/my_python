"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.

示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
"""


class Solution:
    def num_squares(self, n: int) -> int:
        # bfs
        if n == 0:
            return 0
        q = [(n, 0)]
        visited = [False for _ in range(n + 1)]
        visited[n] = True

        while any(q):  # any: if all elements are False, return False, else return True
            num, step = q.pop(0)

            i = 1
            num1 = num - i**2
            while num1 >= 0:
                if num1 == 0:
                    return step + 1
                if not visited[num1]:
                    q.append((num1, step + 1))
                    visited[num1] = True

                i += 1
                num1 = num - i**2

