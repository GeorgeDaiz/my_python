"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树:[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]

提示：
节点总数 <= 1000
"""
from typing import List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, deque = [], collections.deque([root])
        while deque:
            bfs = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2 == 0:
                    bfs.append(node.val)
                else:
                    bfs.appendleft(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(bfs))
        return res
