"""
227. 基本计算器 II
实现一个基本的计算器来计算一个简单的字符串表达式的值。
字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格。 整数除法仅保留整数部分。

示例1:
输入: "3+2*2"
输出: 7

示例 2:
输入: " 3/2 "
输出: 1

示例 3:
输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        # 使用list.pop()在超长测试用例上会超时
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if ((not s[i].isdigit()) and s[i] != ' ') or (i == len(s) - 1):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = s[i]
                num = 0
        return sum(stack)
