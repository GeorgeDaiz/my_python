"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：
输入：nums = [3,4,3,3]
输出：4

示例 2：
输入：nums = [9,1,7,9,7,9,7]
输出：1

限制：
1 <= nums.length <= 10000
1 <= nums[i] < 2^31
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for i in range(32):
                counts[i] += num & 1  # 更新第 i 位 1 的个数之和
                num >>= 1  # 第 i 位 --> 第 i 位
        res, m = 0, 3
        for i in range(31, -1, -1):
            res <<= 1
            res |= counts[i] % m  # 恢复第 i 位
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)

    def singleNumber1(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
