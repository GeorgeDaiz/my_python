"""
Description：

Given an array and a value, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Translate：

给出一个数组和一个特殊值，移出所有和这个特殊值相同的元素并返回新数组的长度。
不能分配额外的空间给其他的数组，你必须在O（1）的空间复杂度里完成这个算法。
数组里的元素顺序可以改变。不管后面输出的新长度是多少都没关系。

Example:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.

"""


class Solution(object):
    @staticmethod
    def remove_element(item, target):
        new_tail = 0
        for i in range(1, len(item)):
            if item[i] != target:
                item[new_tail] = item[i]
                i += 1
        return new_tail
