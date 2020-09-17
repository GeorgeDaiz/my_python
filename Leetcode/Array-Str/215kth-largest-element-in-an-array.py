"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]


class Solution1:
    # 快排
    def findKthLargest(self, nums: list, k: int) -> int or None:
        n = len(nums)
        if k > n:
            return None
        index = self.quick_sort(nums, 0, n-1, k)
        return nums[index]

    def quick_sort(self, nums, l, r, k):
        if l > r:
            return l
        p = self.partition(nums, l, r)
        if p+1 == k:
            return p
        if p+1 > k:
            return self.quick_sort(nums, l, p-1, k)
        else:
            return self.quick_sort(nums, p+1, r, k)

    def partition(self, nums, l, r):
        v = nums[l]
        j = l
        i = l + 1
        while i <= r:
            if nums[i] > v:
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j += 1
            i += 1
        nums[l], nums[j] = nums[j], nums[l]
        return j
