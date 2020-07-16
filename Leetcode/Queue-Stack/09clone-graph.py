"""
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

测试用例格式：

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。

邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。
"""
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def __init__(self):
        self.hash_map = {}

    def clone_graph_dfs(self, node: 'Node') -> 'Node':
        if not node:
            return node

        res = Node(node.val)
        self.hash_map[node.val] = res

        for ne in node.neighbors:
            if ne.val not in self.hash_map:
                res.neighbors.append(self.clone_graph_dfs(ne))
            else:
                res.neighbors.append(self.hash_map[ne.val])
        return res

    @staticmethod
    def clone_graph_bfs(node: 'Node') -> 'Node':
        if not node:
            return node
        hash_map = {}
        queue = [node]
        hash_map[node.val] = Node(node.val)
        while queue:
            curr = queue.pop(0)
            for ne in curr.neighbors:
                if ne.val not in hash_map:
                    hash_map[curr.val].neighbors.append(Node(ne.val))
                    hash_map[ne.val] = Node(ne.val)
                    queue.append(ne)
                else:
                    hash_map[curr.val].neighbors.append(hash_map[ne.val])
        return Node(node.val)

    @staticmethod
    def clone_graph1(node: 'Node') -> 'Node':
        if not node:
            return node

        queue = deque([node])
        visited = {node: Node(node.val, [])}
        while queue:
            n = queue.popleft()
            for ne in n.neighbors:
                if ne not in visited:
                    visited[ne] = Node(ne.val, [])
                    queue.append(ne)

                visited[n].neighbors.append(visited[ne])
        return visited[node]
