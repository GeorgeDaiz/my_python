"""
140.单词拆分II
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
 "cats and dog",
 "cat sand dog"
]

示例 2：
输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
 "pine apple pen apple",
 "pineapple pen apple",
 "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。

示例3：
输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import functools


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @functools.lru_cache(None)
        def backtrack(index: int) -> List[List[str]]:
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index: i]
                if word in wordDict:
                    next_word_break = backtrack(i)
                    for next_word in next_word_break:
                        ans.append(next_word.copy() + [word])
            return ans

        word_set = set(wordDict)
        break_list = backtrack(0)
        return [" ".join(words[::-1]) for words in break_list]
