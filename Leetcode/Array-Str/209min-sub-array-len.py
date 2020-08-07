"""
给定一个含有n个正整数的数组和一个正整数s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组[4,3]是该条件下的长度最小的子数组。

进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""


class Solution:
    @staticmethod
    def min_sub_array_len(self, s: int, nums: [int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        l, r = 0, 0
        count = 0
        res = float('inf')
        while r < n:
            count += nums[r]
            while count >= s:
                res = min(res, r - l + 1)
                count -= nums[l]
                l += 1
            r += 1
        return res if res != float('inf') else 0
