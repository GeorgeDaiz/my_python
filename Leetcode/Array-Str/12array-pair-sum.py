"""
给定长度为2n的数组, 你的任务是将这些数分成n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到n 的 min(ai, bi) 总和最大。

示例 1:

输入: [1,4,3,2]

输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
提示:

n是正整数,范围在 [1, 10000].
数组中的元素范围在 [-10000, 10000].
"""


class Solution:
    @staticmethod
    def array_pair_sum(nums) -> int:
        nums_sorted = sorted(nums)
        i = 0
        res = 0
        while i < len(nums_sorted):
            res += nums_sorted[i]
            i += 2

        return res


if __name__ == '__main__':
    ret = Solution().array_pair_sum([1, 4, 3, 2])
    print(ret)
