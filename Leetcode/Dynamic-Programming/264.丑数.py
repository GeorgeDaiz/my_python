"""
264.丑数II
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含2, 3, 5 的正整数。

示例:
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:
1是丑数。
n不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1, ]
        t2, t3, t5 = 0, 0, 0
        for i in range(n-1):
            res.append(min(res[t2]*2, res[t3]*3, res[t5]*5))
            if res[-1] == res[t2]*2:
                t2 += 1
            if res[-1] == res[t3]*3:
                t3 += 1
            if res[-1] == res[t5]*5:
                t5 += 1
        return res[-1]
