"""
154. 寻找旋转排序数组中的最小值 II
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组[0,1,2,4,5,6,7] 可能变为[4,5,6,7,0,1,2])。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：
输入: [1,3,5]
输出: 1

示例2：
输入: [2,2,2,0,1]
输出: 0
说明：

这道题是寻找旋转排序数组中的最小值的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return None
        l, r = 0, len(numbers)-1
        while l < r:
            mid = (l+r)//2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                return min(numbers[l:r])
        return numbers[l]
