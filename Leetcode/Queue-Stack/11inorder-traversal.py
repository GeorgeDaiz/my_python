"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []

    def inorder_traversal(self, root: TreeNode) -> 'List[int]':
        if not root:
            return []

        self.inorder_traversal(root.left)
        self.res.append(root.val)
        self.inorder_traversal(root.right)

        return self.res

    def inorder_traversal1(self, root: TreeNode) -> 'List[int]':
        if not root:
            return []

        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
