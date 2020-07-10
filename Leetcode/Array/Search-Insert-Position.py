"""
Description：

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Translate：

给一个有序的数组和一个目标值，返回这个目标值在数组里的位置索引。如果找不到，请返回目标值如果在这个有序数列中的索引。
这个数组里没有重复的元素。

Example:
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1

Input: [1,3,5,6], 7
Output: 4

Input: [1,3,5,6], 0
Output: 0
"""


# 二分法
def search_insert(item, target):
    low = 0
    high = len(item) - 1
    while low <= high:
        mid = (low + high) / 2
        if item[mid] == target:
            return mid
        elif item[mid] < target:
            low = mid + 1
        elif item[mid] > target:
            high = mid - 1
    return low
