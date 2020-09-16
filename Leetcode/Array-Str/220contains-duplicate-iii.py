"""
在整数数组 nums 中，是否存在两个下标 i 和 j，使得nums [i] 和nums [j]的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。

如果存在则返回 true，不存在返回 false。

示例1:
输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:
输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
        # 桶排序
        if len(nums) == 0 or k == 0:
            return False
        bucket = dict()
        if t < 0:
            return False
        for i in range(len(nums)):
            nth = nums[i] // (t + 1)
            if nth in bucket:
                return True
            if nth - 1 in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return True
            if nth + 1 in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return True
            bucket[nth] = nums[i]
            if i >= k:
                bucket.pop(nums[i - k] // (t + 1))
        return False

    def containsNearbyAlmostDuplicate1(self, nums: list, k: int, t: int) -> bool:
        if len(nums) == 0 or k == 0:
            return False
        for i in range(len(nums)-1):
            for j in range(i+1, min(len(nums), i+k+1)):
                if abs(nums[j] - nums[i]) <= t:
                    return True
        return False

    def containsNearbyAlmostDuplicate2(self, nums: list, k: int, t: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        record = set()  # 定义窗口
        for i in range(n):
            if t == 0:  # 如果t=0，那么看看窗口内是否有重复元素，有就返回True
                if nums[i] in record:
                    return True
            else:
                for j in record:  # 遍历窗口元素，判断是否有绝对值小于t的情况，有就返回True
                    if abs(j - nums[i]) <= t:
                        return True
            record.add(nums[i])  # 向集合添加元素
            if len(record) > k:
                record.remove(nums[i - k])  # 维护长度为k的窗口
        return False
