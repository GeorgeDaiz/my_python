"""
79.单词搜索

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()

        def backtrack(i, j, cur):
            if board[i][j] != word[cur]:
                return False
            if cur == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for dir in dirs:
                ni, nj = i + dir[0], j + dir[1]
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    if (ni, nj) not in visited:
                        if backtrack(ni, nj, cur+1):
                            result = True
                            break
            visited.remove((i, j))
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False

    def exist1(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            res = dfs(i-1, j, k+1) or dfs(i, j-1, k+1) or dfs(i+1, j, k+1) or dfs(i, j+1, k+1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    ret = Solution().exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE')
    print(ret)
