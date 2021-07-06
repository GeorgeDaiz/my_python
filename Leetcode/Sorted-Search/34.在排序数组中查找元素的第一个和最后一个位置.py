"""
34.在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是O(log n) 级别。

如果数组中不存在目标值，返回[-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 官方题解
        def helper(flag):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target or (flag and target == nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            return left

        left = helper(True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, helper(False) - 1]

    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = self.search_left(nums, target)
        if left == -1:
            return [-1, -1]

        right = self.search_right(nums, target)
        return [left, right]

    def search_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if left != len(nums) and nums[left] == target:
            return left
        return -1

    def search_right(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return right


if __name__ == '__main__':
    ret = Solution().searchRange1([2, 2], 3)
    print(ret)
