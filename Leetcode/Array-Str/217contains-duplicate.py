"""
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
"""


class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        # 排序再遍历O(n)
        if len(nums) <= 1:
            return False
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False

    def containsDuplicate1(self, nums: list) -> bool:
        # 使用dict记录
        dic = {}
        for i in nums:
            if i in dic:
                return True
            else:
                dic[i] = 1
        return False

    def containsDuplicate2(self, nums: list) -> bool:
        return len(set(nums)) != len(nums)