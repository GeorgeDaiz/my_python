"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1:
输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1
"""
import collections


class Solution:
    def num_islands_dfs(self, grid) -> int:
        # DFS
        res = 0
        if len(grid) == 0:
            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    # self.bfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        # 已知当前点为1，将他周围相邻的所有1转为0
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 方向数组
        grid[i][j] = '0'
        for d in dirs:  # 遍历上下左右四个方向
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                if grid[ni][nj] == '1':
                    self.dfs(grid, ni, nj)

    @staticmethod
    def num_islands_bfs(grid) -> int:
        # BFS
        res = 0
        if len(grid) == 0:
            return res

        queue = collections.deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    queue.append((i, j))
                    grid[i][j] = '0'

                    while queue:
                        x, y = queue.popleft()
                        for m, n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                            if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == '1':
                                queue.append((m, n))
                                grid[m][n] = '0'
        return res

    def bfs(self, grid, i, j):
        # 已知当前点为1，将他周围相邻的所有1转为0
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 方向数组
        grid[i][j] = '0'
        s = []
        s.append([i, j])
        while s:
            temp = s.pop(0)
            x, y = temp[0], temp[1]
            for m, n in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == '1':
                    s.append((m, n))
                    grid[m][n] = '0'
