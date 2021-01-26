"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定二叉树: root =[3,5,1,6,2,0,8,null,null,7,4]

示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    解题思路：
    祖先的定义： 若节点 p 在节点 root 的左（右）子树中，或 p=root ，则称 root 是 p 的祖先。
    最近公共祖先的定义： 设节点 root 为节点 p,q 的某公共祖先，若其左子节点 root.left 和右子节点root.right 都不是 p,q 的公共祖先，则称 root 是 “最近的公共祖先” 。

    根据以上定义，若 root 是 p,q 的 最近公共祖先 ，则只可能为以下情况之一：

    1.p 和 q 在 root 的子树中，且分列 root 的 异侧（即分别在左、右子树中）；
    2.p=root ，且 q 在 root 的左或右子树中；
    3.q=root ，且 p 在 root 的左或右子树中；
    考虑通过递归对二叉树进行后序遍历，当遇到节点 p 或 q 时返回。从底至顶回溯，当节点 p,q 在节点 root 的异侧时，节点 root 即为最近公共祖先，则向上返回 root 。
    递归解析：
    终止条件：
    1.当越过叶节点，则直接返回 null ；
    2.当 root 等于 p,q ，则直接返回 root ；
    递推工作：
    1.开启递归左子节点，返回值记为 left ；
    2.开启递归右子节点，返回值记为 right ；
    返回值： 根据 left 和 right ，可展开为四种情况；
    1.当 left 和 right 同时为空 ：说明 root 的左 / 右子树中都不包含 p,q ，返回 null ；
    2.当 left 和 right 同时不为空 ：说明 p,q 分列在 root 的 异侧 （分别在 左 / 右子树），因此 root 为最近公共祖先，返回 root ；
    3.当 left 为空 ，right 不为空 ：p,q 都不在 root 的左子树中，直接返回 right 。具体可分为两种情况：
        1)p,q 其中一个在 root 的 右子树 中，此时 right 指向 p（假设为 p）；
        2)p,q 两节点都在 root 的 右子树 中，此时的 right 指向 最近公共祖先节点 ；
    当 left 不为空 ，right 为空 ：与情况 3. 同理；
    """
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root
