"""
在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
给定行数N和序数 K，返回第 N 行中第 K个字符。（K从1开始）

例子:

输入: N = 1, K = 1
输出: 0

输入: N = 2, K = 1
输出: 0

输入: N = 2, K = 2
输出: 1

输入: N = 4, K = 5
输出: 1

解释:
第一行: 0
第二行: 01
第三行: 0110
第四行: 01101001

注意：

N的范围[1, 30].
K的范围[1, 2^(N-1)].
"""


class Solution:
    def kth_grammar(self, N: int, K: int) -> int:
        if N <= 2:
            return K-1
        if K % 2 == 0:
            return abs(self.kth_grammar(N - 1, K // 2) - 1)
        else:
            return self.kth_grammar(N - 1, (K + 1) // 2)


if __name__ == '__main__':
    res = Solution().kth_grammar(3, 2)
    print(res)
