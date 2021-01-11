"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是

"""


class Solution:
    def isNumber(self, s: str) -> bool:
        status = [
            {'': 0, 's': 1, 'd': 2, '.': 4},    # start with 'blank'
            {'d': 2, '.': 4},                   # 'sign' before 'e'
            {'d': 2, '.': 3, 'e': 5, ' ': 8},   # 'digit' before 'dot'
            {'d': 3, 'e': 5, ' ': 8},           # 'digit' after 'dot'
            {'d': 3},                           # 'dot' before 'digit' ('dot' after 'blank')
            {'s': 6, 'd': 7},                   # 'e'
            {'d': 7},                           # 'sign' after 'e'
            {'d': 7, ' ': 8},                   # 'digit' after 'e'
            {' ': 8}                            # end with 'blank'
        ]
        p = 0
        for c in s:
            if '0' <= c <= '9':
                t = 'd'
            elif c in '+-':
                t = 'sign'
            elif c in 'eE':
                t = 'e'
            elif c in '.':
                t = c
            else:
                t = '?'
            if t not in status[p]:
                return False
            p = status[p][t]
        return p in (2, 3, 7, 8)
