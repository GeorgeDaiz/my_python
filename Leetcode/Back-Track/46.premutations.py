"""
46.全排列

给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        res = []
        n = len(nums)
        visited = [0] * n

        # 1
        def backtrack(temp_list, length):
            if length == n:
                res.append(temp_list)
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = 1
                backtrack(temp_list+[nums[i]], length+1)
                visited[i] = 0

        # 2
        # def backtrack1(nums, temp_list, length):
        #     if length == n:
        #         res.append(temp_list)
        #     for i in range(len(nums)):
        #         backtrack1(nums[:i]+nums[i+1:], temp_list+[nums[i]], length+1)

        backtrack([], 0)
        # backtrack1(nums, [], 0)
        return res

    def permute1(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []

        def backtrack(cur=0):
            if cur == len(nums):
                res.append(nums[:])
                return
            for i in range(cur, len(nums)):
                nums[cur], nums[i] = nums[i], nums[cur]
                backtrack(cur + 1)
                nums[cur], nums[i] = nums[i], nums[cur]

        backtrack()
        return res
