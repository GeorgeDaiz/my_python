"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
"""
import collections


class Solution:
    """
    如果从1找0，复杂度会是O(m^2*n^2)超时，则使用BFS从0找1
    """
    @staticmethod
    def update_matrix(matrix) -> 'list':
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        que = collections.deque()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    que.append((i, j))
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        print(que)
        while que:
            pos = que.popleft()
            for d in directions:
                new_x, new_y = pos[0] + d[0], pos[1] + d[1]
                if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] == 1:
                    if dist[new_x][new_y] < dist[pos[0]][pos[1]] + 1:
                        dist[new_x][new_y] = dist[pos[0]][pos[1]] + 1
                        que.append((new_x, new_y))

        return dist


if __name__ == '__main__':
    s = Solution()
    res = s.update_matrix(matrix=[[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print(res)
