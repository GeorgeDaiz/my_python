"""
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

限制：
1 <= s 的长度 <= 8
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s:
            return []
        res, sli = [], list(s)

        def back_track(length):
            if length == len(s) - 1:
                res.append(''.join(sli))
                return
            visited = set()
            for i in range(length, len(sli)):
                if sli[i] in visited:
                    continue
                visited.add(sli[i])
                sli[i], sli[length] = sli[length], sli[i]
                back_track(length+1)
                sli[i], sli[length] = sli[length], sli[i]
        back_track(0)
        return res


if __name__ == '__main__':
    ret = Solution().permutation('aab')
    print(ret)
