"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果n是3的倍数，输出“Fizz”；

2. 如果n是5的倍数，输出“Buzz”；

3.如果n同时是3和5的倍数，输出 “FizzBuzz”。

示例：
n = 15,
返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution:
    def fizzBuzz(self, n: int) -> list:
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res


if __name__ == '__main__':
    ret = Solution().fizzBuzz(15)
    print(ret)
