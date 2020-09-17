"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0)。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且n的值至少为 2。

示例：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
"""


class Solution:
    def maxArea(self, height: list) -> int:
        i = 0
        j = len(height) - 1
        h_res = float('-inf')
        while i < j:
            h_res = max(h_res, (j-i) * min(height[i], height[j]))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return h_res
