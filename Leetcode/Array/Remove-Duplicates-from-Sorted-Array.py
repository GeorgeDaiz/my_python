"""
Description：

Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Translate：

给定一个有序数组，删除重复内容，使每个元素只出现一次，并返回新的长度。
不要为其他数组分配额外的空间，你必须在O（1）的空间里完成这个功能。

Example:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

"""


class Solution(object):
    def remove_duplicates(self, item):
        if not item:
            return 0

        new_tail = 0
        for i in range(1, len(item)):
            if item[i] != item[new_tail]:
                new_tail += 1
                item[new_tail] = item[i]

        return new_tail+1
