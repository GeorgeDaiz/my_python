"""
322.零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

示例1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

示例 4：
输入：coins = [1], amount = 1
输出：1

示例 5：
输入：coins = [1], amount = 2
输出：2
"""
import functools
from typing import List


class Solution:
    # 动态规划，自上而下
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem-coin)
                if 0 <= res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1
        self.coins = coins
        if amount < 1:
            return 0
        return dp(amount)

    # 动态规划，自下而上
    def coinChange1(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)
        return dp[amount] if dp[amount] != float("inf") else -1

    # dfs+剪枝
    def coinChange2(self, coins: List[int], amount: int) -> int:
        def dfs(coind, amount, count):
            if amount == 0:
                self.ans = min(self.ans, count)
                return
            if coind >= len(coins):
                return
            for i in range(amount // coins[coind], -1, -1):
                if i + count < self.ans:
                    dfs(coind+1, amount-coins[coind]*i, count+i)
                else:
                    break
        self.ans = float('inf')
        coins = sorted(coins, reverse=True)
        dfs(0, amount, 0)
        return self.ans if self.ans != float('inf') else -1
