"""
实现pow(x, n)，即计算 x 的 n 次幂函数。

示例 1:
输入: 2.00000, 10
输出: 1024.00000

示例2:
输入: 2.10000, 3
输出: 9.26100

示例3:
输入: 2.00000, -2
输出: 0.25000

说明:
-100.0 <x< 100.0
n是 32 位有符号整数，其数值范围是[−231,231− 1] 。
"""


class Solution:
    @staticmethod
    def my_pow(x: float, n: int) -> float:
        def quick_mul(N):
            if N == 0:
                return 1.0
            y = quick_mul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quick_mul(n) if n >= 0 else 1.0 / quick_mul(-n)

    @staticmethod
    def my_pow1(x: float, n: int) -> float:
        def quick_mul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quick_mul(n) if n >= 0 else 1.0 / quick_mul(-n)


if __name__ == '__main__':
    res = Solution().my_pow(1.00001, 123456)
    print(res)
