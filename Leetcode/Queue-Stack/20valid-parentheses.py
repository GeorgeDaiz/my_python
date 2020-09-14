"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

示例 2:

输入: "()[]{}"
输出: true

示例 3:

输入: "(]"
输出: false

示例 4:

输入: "([)]"
输出: false

示例 5:

输入: "{[]}"
输出: true
"""


class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        b = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for x in s:
            if x in b:
                stack.append(x)
            else:
                if stack and x == b[stack.pop()]:
                    continue
                else:
                    return False
        if stack:
            return False
        else:
            return True
