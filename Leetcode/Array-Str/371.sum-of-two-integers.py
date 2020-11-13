"""
371.两整数之和
不使用运算符+ 和-，计算两整数a、b之和。

示例 1:
输入: a = 1, b = 2
输出: 3

示例 2:
输入: a = -2, b = 3
输出: 1
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 3^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1
            # 取余范围限制在[0, 3^32-1]范围内
            a = (a ^ b) % MASK
            b = carry % MASK

        return a if a < MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
