"""
169.多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于⌊ n/2 ⌋的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例1:
输入: [3,2,3]
输出: 3

示例2:
输入: [2,2,1,1,1,2,2]
输出: 2
"""
from typing import List
import collections


class Solution:
    # 暴力法
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        target = len(nums) / 2
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 0
            if dic[nums[i]] + 1 > target:
                return nums[i]
            else:
                dic[nums[i]] += 1

    # 哈希表
    def majorityElement1(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    # 排序法
    def majorityElement2(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

    # Boyer-Moore 投票算法
    def majorityElement3(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


Solution().majorityElement1([1, 2, 3, 3, 3])
