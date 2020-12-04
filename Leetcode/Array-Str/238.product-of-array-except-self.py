"""
238.除自身之外数组的乘积
给你一个长度为n的整数数组nums，其中n > 1，返回输出数组output，其中 output[i]等于nums中除nums[i]之外其余各元素的乘积。

示例:
输入: [1,2,3,4]
输出: [24,12,8,6]

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
"""
from typing import List
from functools import reduce


def my_multiply(x, y):
    return x * y


class Solution:
    # 左右乘积列表
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mul, r_mul, ans = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        l_mul[0] = 1
        r_mul[len(nums) - 1] = 1
        for i in range(len(nums)):
            l_mul[i] = l_mul[i-1] * nums[i-1]

        for i in reversed(range(len(nums) - 1)):
            r_mul[i] = r_mul[i+1] * nums[i+1]

        for i in range(len(ans)):
            ans[i] = l_mul[i] * r_mul[i]

        return ans

    # 空间复杂度O(1)方法
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length
        ans[0] = 1
        for i in range(1, length):
            ans[i] = ans[i-1] * nums[i-1]

        right = 1
        for i in reversed(range(length)):
            ans[i] *= right
            right *= nums[i]

        return ans


if __name__ == '__main__':
    ret = Solution().productExceptSelf1([1, 2, 3, 4])
    print(ret)
