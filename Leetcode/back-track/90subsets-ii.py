"""
90.子集II

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def backtrack(temp, cur):
            res.append(temp)
            for i in range(cur, n):
                if i > cur and nums[i] == nums[i-1]:
                    continue
                backtrack(temp+nums[i], cur+1)

        backtrack([], 0)
        return res
