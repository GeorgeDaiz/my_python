"""
279.完全平方数
给定正整数n，找到若干个完全平方数（比如1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例1：
输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

提示：
1 <= n <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 背包DP
    def numSquares(self, n: int) -> int:
        dp = [i * i for i in range(1, int(n ** 0.5) + 1)]
        f = [0] + [float('inf')] * n
        for num in dp:
            for j in range(num, n + 1):
                f[j] = min(f[j], f[j - num] + 1)
        return f[-1]

    # 贪心算法
    def numSquares1(self, n: int) -> int:
        dp = set([i * i for i in range(1, int(n ** 0.5) + 1)])

        def divisible(n, count):
            if count == 1:
                return n in dp
            for p in dp:
                if divisible(n - p, count - 1):
                    return True
            return False

        for count in range(1, n + 1):
            if divisible(n, count):
                return count
