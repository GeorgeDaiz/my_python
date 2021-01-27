"""
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出
前序遍历 preorder =[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def build_tree(self, preorder: list, inorder: list) -> TreeNode or None:
        if not inorder or not preorder:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])

        root.left = self.build_tree(preorder[1: idx + 1], inorder[: idx])
        root.right = self.build_tree(preorder[idx + 1:], inorder[idx + 1:])

        return root

    @staticmethod
    def build_tree1(preorder: list, inorder: list) -> TreeNode or None:
        if not inorder or not preorder:
            return None

        idx_map = {val: idx for idx, val in enumerate(inorder)}

        def search(left, right):
            if left > right:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            idx = idx_map[val]
            root.left = search(left, idx - 1)
            root.right = search(idx + 1, right)
            return root

        return search(0, len(inorder) - 1)
