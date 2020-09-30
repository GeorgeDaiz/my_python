"""
78.子集

给定一组不含重复元素的整数数组nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
 [3],
 [1],
 [2],
 [1,2,3],
 [1,3],
 [2,3],
 [1,2],
 []
]
"""
from typing import List
import itertools


class Solution:
    def subsets(self, nums: List[int]):
        # 库函数
        res = []
        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        # 迭代
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        res = []
        n = len(nums)

        def backtrack(temp, cur):
            res.append(temp)
            for i in range(cur, n):
                backtrack(temp+[nums[i]], cur+1)

        backtrack([], 0)
        return res


if __name__ == '__main__':
    ret = Solution().subsets2([2, 3, 4, 5])
    print(ret)
