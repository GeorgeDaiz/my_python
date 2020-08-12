"""
从中序与后序遍历序列构造二叉树
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder =[9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
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
    def build_tree(self, inorder: list, postorder: list) -> TreeNode:
        if not postorder:
            return TreeNode(None)

        root = TreeNode(postorder[-1])

        root_index = inorder.index(postorder[-1])

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        l_left = len(left_inorder)

        left_postorder = postorder[:l_left]
        right_postorder = postorder[l_left: -1]

        root.left = self.build_tree(left_inorder, left_postorder)
        root.right = self.build_tree(right_inorder, right_postorder)

        return root

    @staticmethod
    def build_tree1(inorder: list, postorder: list) -> TreeNode:
        if not inorder:
            return TreeNode(None)
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        def search(left, right):
            if left > right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            idx = idx_map[val]
            root.right = search(idx + 1, right)
            root.left = search(left, idx - 1)
            return root

        return search(0, len(inorder) - 1)
