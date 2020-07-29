import collections


class Solution:
    @staticmethod
    def flood_fill(image, sr: int, sc: int, new_color: int) -> 'list':
        i, j = len(image), len(image[0])
        color = image[sr][sc]
        if color == new_color:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = new_color
                if r >= 1:
                    dfs(r - 1, c)
                if r < i - 1:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c < j - 1:
                    dfs(r, c + 1)
        dfs(sr, sc)
        return image

    @staticmethod
    def flood_fill_bfs(image, sr, sc, new_color):
        que = collections.deque()
        que.append((sr, sc))
        start = image[sr][sc]
        if start == new_color:
            return image
        i, j = len(image), len(image[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while que:
            pos = que.popleft()
            image[pos[0]][pos[1]] = new_color
            for d in directions:
                new_x, new_y = pos[0] + d[0], pos[1] + d[1]
                if 0 <= new_x < i and 0 <= new_y < j and image[new_y][new_y] == start:
                    que.append((new_x, new_y))

        return image
