"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

示例1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3

解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = []
        max_len = 0
        for i in range(len(s)):
            if s[i] not in res:
                res.append(s[i])
                max_len = max(max_len, len(res))
            else:
                res = res[res.index(s[i]) + 1:]
                res.append(s[i])
        return max_len


if __name__ == '__main__':
    ret = Solution().lengthOfLongestSubstring("qjroijwqoijrpajfp")
    print(ret)

