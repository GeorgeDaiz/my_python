"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明:叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        ret, path = [], []

        def dfs(node, res):
            if not node:
                return
            path.append(node.val)
            res -= node.val
            if not node.left and not node.right and res == 0:
                ret.append(path[:])
            dfs(node.left, res)
            dfs(node.right, res)
            path.pop()

        dfs(root, total)
        return ret
