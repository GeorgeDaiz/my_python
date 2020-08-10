"""
对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树[1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def is_symmetric(root: TreeNode) -> bool:
        # DFS
        if not root:
            return True

        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)

    @staticmethod
    def is_symmetric1(root: TreeNode) -> bool:
        # # BFS1
        # if not root:
        #     return True
        # queue = deque()
        # queue.append(root.left)
        # queue.append(root.right)
        # while queue:
        #     left, right = queue.popleft(), queue.popleft()
        #     if not left and not right:
        #         continue
        #     if not left or not right:
        #         return False
        #     if left.val != right.val:
        #         return False
        #     queue.append(left.left)
        #     queue.append(right.right)
        #     queue.append(left.right)
        #     queue.append(right.left)
        # return True

        # BFS2
        if not root:
            return True
        queue = deque()
        queue.append((root, root))
        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True
