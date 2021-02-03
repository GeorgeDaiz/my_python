"""
在无限的整数序列1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第n 位数字。

注意：n是正数且在 32 位整数范围内（n < 231）。

示例 1：
输入：3
输出：3

示例 2：
输入：11
输出：0
解释：第 11 位数字在序列 '123456789101112...', 里是 0 ，它是 10 的一部分。
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start = 1, 1
        index_count = digit * start * 9
        while n > index_count:
            n -= index_count
            digit += 1
            start *= 10
            index_count = digit * start * 9

        num = start + (n - 1) // digit
        remainder = (n - 1) % digit
        return int(str(num)[remainder])


res = Solution().findNthDigit(10)
print(res)
