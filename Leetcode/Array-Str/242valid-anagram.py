"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)

        return s_count == t_count

    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            d[c] = d.get(c, 0) - 1
            if d[c] < 0:
                return False

        return True
