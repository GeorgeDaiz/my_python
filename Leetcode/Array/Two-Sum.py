"""
1.Two-Sum
Description：

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Translate：

给一组整数，返回两个之和等于给定的特殊目标值的数的索引。
你可以假设每个输入将有一个确切的解决方案，但您不能使用相同元素的两次。

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        if len(nums) <= 1:
            return False

        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
