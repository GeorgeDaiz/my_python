"""
统计所有小于非负整数 n 的质数的数量。

示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""
import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        # 暴力算法
        def helper(num):
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return False
            return True

        res = 0
        for num in range(2, n):
            print(num, helper(num))
            if helper(num):
                res += 1
        return res

    def countPrimes1(self, n: int) -> int:
        # 埃拉托斯特尼筛法
        if n < 2:
            return 0
        is_prime = [1] * n
        is_prime[0] = is_prime[1] = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                is_prime[i*i: n: i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(is_prime)


if __name__ == '__main__':
    res = Solution().countPrimes1(10)
    print(res)
