"""
17.电话号码的字母组合

给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
import itertools


class Solution:
    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrace(index=0):
            if index == len(digits):
                print(combination)
                combinations.append(''.join(combination))
            else:
                digit = digits[index]
                for letter in phone_map[digit]:
                    combination.append(letter)
                    backtrace(index+1)
                    combination.pop()

        combination = []
        combinations = []
        backtrace()
        return combinations

    def letterCombinations1(self, digits: str) -> list:
        if not digits:
            return []
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        groups = (phone_map[digit] for digit in digits)
        return ["".join(combination) for combination in itertools.product(*groups)]


if __name__ == '__main__':
    Solution().letterCombinations('234')
