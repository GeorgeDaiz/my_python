"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


class Solution:
    @staticmethod
    def longestCommonPrefix(strs) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        res = ""
        min_len = min([len(i) for i in strs])
        for i in range(min_len):
            cur = set(word[i] for word in strs)
            if len(cur) == 1:
                res += cur.pop()
            else:
                break
        return res


if __name__ == '__main__':
    ret = Solution().longestCommonPrefix(["aca", "cba"])
    print(ret)
