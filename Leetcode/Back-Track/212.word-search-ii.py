"""
212. 单词搜索 II
给定一个m x n 二维字符网格board和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例 1：
输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
输出：["eat","oath"]

示例 2：
输入：board = [["a","b"],["c","d"]], words = ["abcb"]
输出：[]

提示：
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] 是一个小写英文字母
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] 由小写英文字母组成
words 中的所有字符串互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word

        row_num = len(board)
        col_num = len(board[0])

        matched_words = []

        def backtrack(row, col, parent):
            letter = board[row][col]
            curr = parent[letter]
            word_match = curr.pop(WORD_KEY, False)
            if word_match:
                matched_words.append(word_match)
            board[row][col] = '#'
            for (row_off, col_off) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + row_off, col + col_off
                if new_row < 0 or new_row >= row_num or new_col < 0 or new_col >= col_num:
                    continue
                if not board[new_row][new_col] in curr:
                    continue
                backtrack(new_row, new_col, curr)

            board[row][col] = letter
            if not curr:
                parent.pop(letter)

        for row in range(row_num):
            for col in range(col_num):
                if board[row][col] in trie:
                    backtrack(row, col, trie)

        return matched_words


if __name__ == '__main__':
    ret = Solution().findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"])
    print(ret)
