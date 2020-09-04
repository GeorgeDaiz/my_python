"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为[−231, 231− 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res

    def reverse1(self, x: int) -> int:
        s = str(abs(x))
        s = s[::-1]
        if x < 0:
            s = '-' + s
        result = int(s)
        if -2 ** 31 <= result <= 2**31:
            return result
        else:
            return 0
