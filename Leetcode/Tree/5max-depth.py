"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明:叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        # 递归
        if not root:
            return 0
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        depth = max(left_depth, right_depth) + 1
        return depth

    @staticmethod
    def max_depth1(root):
        # 迭代
        de = 0
        if root:
            stack = [(1, root)]
        else:
            return 0
        while stack:
            cur_de, node = stack.pop()
            if node:  # 只有当结点存在时+1后的深度才会被采用
                de = max(de, cur_de)
                stack.append((cur_de + 1, node.left))
                stack.append((cur_de + 1, node.right))
        return de
