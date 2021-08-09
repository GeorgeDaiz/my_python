"""
149.直线上最多的点数
给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。

示例 1：
输入：points = [[1,1],[2,2],[3,3]]
输出：3

示例 2：
输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4

提示：
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
points 中的所有点 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-points-on-a-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n
        ans = 0

        def gcd(a, b) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        for i in range(n - 1):
            hash_map = defaultdict(lambda: 0)
            for j in range(i + 1, n):
                a = points[i][1] - points[j][1]
                b = points[i][0] - points[j][0]
                gcd_ab = gcd(a, b)
                key = tuple((a // gcd_ab, b // gcd_ab))
                hash_map[key] += 1
            max_alignment = max(hash_map.values())
            ans = max(ans, max_alignment + 1)
        return ans
