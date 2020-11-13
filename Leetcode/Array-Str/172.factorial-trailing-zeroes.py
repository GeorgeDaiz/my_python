"""
172.阶乘后的0
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:
输入: 3
输出: 0
解释:3! = 6, 尾数中没有零。

示例2:
输入: 5
输出: 1
解释:5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为O(logn)。
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 计算因子5
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count

