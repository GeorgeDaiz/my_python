"""
摇摆序列(leetcode376)

题目：一个整数序列，如果两个相邻元素的差恰好正负(负正)交替出现，则该序列呗成为摇摆序列，一个小于2个元素的序列直接为摇摆序列，给一个随机序列，求这个序列满足摇摆序列定义的最长子序列的长度。
例如：
序列[1,7,4,9,2,5],相邻元素的差(6,-3,5,-7,3),该序列为摇摆序列
序列[1,4,7,2,5]相差(3,3,-5,3)不是摇摆序列

思考与分析：

[1,17,5,10,13,15,10,5,16,8]，整体不是摇摆序列，但是我们观察该序列的前6位：[1,17,5,10,13,15…];5,10,13,15部分为上升段，其中有三个子序列是摇摆序列：
[1,17,5,10….]
[1,17,5,13,…]
[1,17,5,15…..]
在不清楚原始序列的7为是什么的情况下，只看前6位，摇摆子系列的第四位从10，13，15中选择一个数，我们应该选择那一个？

应该选择使得摇摆子序列长度更长的数，所以应该是15，这样遇到比他小的数的可能性就会大一点，按照这种思路总结出贪心规律

贪心规律：

当序列有一段连续的递增(或递减)时，为形成摇摆子序列，我们只需要保留这段连续的递增(或递减)的首尾元素，这样更有可能使得尾部的后一个元素成为摇摆子序列的下一个元素。
"""


class Solution:
    @staticmethod
    def max_length(nums) -> int:
        if len(nums) < 2:
            return len(nums)
        begin = 0
        up = 1
        down = 2
        state = begin
        vision = [up, begin, down]
        max_length = 1
        for i in range(1, len(nums)):
            if state == 0:
                if nums[i - 1] < nums[i]:
                    state = 1
                    max_length += 1
                elif nums[i - 1] > nums[i]:
                    state = 2
                    max_length += 1

            if state == 1:
                if nums[i - 1] > nums[i]:
                    state = 2
                    max_length += 1

            if state == 2:
                if nums[i - 1] < nums[i]:
                    state = 1
                    max_length += 1

        return max_length


if __name__ == '__main__':
    res = Solution().max_length([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
    print(res)

