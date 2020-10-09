"""
35.搜索插入位置
给一个有序的数组和一个目标值，返回这个目标值在数组里的位置索引。如果找不到，请返回目标值如果在这个有序数列中的索引。
这个数组里没有重复的元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
"""


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # 二分法
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return low

    def searchInsert1(self, nums, target: int) -> int:
        # 二分法
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
        return low


if __name__ == '__main__':
    res = Solution().searchInsert([1, 3, 5, 6], 7)
    print(res)
