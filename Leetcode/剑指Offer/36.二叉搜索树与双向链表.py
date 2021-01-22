"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。
对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.pre:
                self.pre.right, node.left = node, self.pre
            else:
                self.head = node
            self.pre = node
            dfs(node.right)

        if not root:
            return
        self.pre= None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
