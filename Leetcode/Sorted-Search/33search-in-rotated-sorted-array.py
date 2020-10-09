"""
33.搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组[0,1,2,4,5,6,7]可能变为[4,5,6,7,0,1,2])。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回-1。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是O(logn) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[-1] < target < nums[0] or not nums:
            return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
