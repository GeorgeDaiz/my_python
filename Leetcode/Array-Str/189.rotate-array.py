"""
给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为O(1) 的原地算法。
"""


class Solution:
    def rotate1(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 暴力法
        def revs(nums):
            temp = nums.pop()
            nums.insert(0, temp)

        for i in range(k % len(nums)):
            revs(nums)

    def rotate2(self, nums: list, k: int) -> None:
        # 切片法
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate3(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 反转法
        def reverse(nums, i, j):
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1
        k %= len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums) - 1)
