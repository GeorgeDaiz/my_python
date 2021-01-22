"""
297.二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例:

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示:这与 LeetCode 目前使用的方式一致。

说明:不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
"""
import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # 层序遍历
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        vals, i = data[1: -1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root


class Codec1:
    # DFS
    def serialize(self, root):
        # Encode a tree to a single string.
        if not root:
            return 'X,'
        left_serilized = self.serialize(root.left)
        right_serilized = self.serialize(root.right)
        return str(root.val) + ',' + left_serilized + right_serilized

    def deserilize(self, data):
        # Decode your encode data to tree
        data = data.split(',')
        root = self.build_tree(data)
        return root

    def build_tree(self, data):
        val = data.pop(0)
        if val == 'X':
            return None
        node = TreeNode(val)
        node.left = self.build_tree(data)
        node.right = self.build_tree(data)
        return node


class Codec2:
    # BFS
    def serilize(self, root):
        if not root:
            return '[]'
        deque = collections.deque(root)
        res = ''
        while deque:
            node = deque.popleft()
            if node != TreeNode(None):
                res += str(node.val) + ','
                deque.append(node.left)
                deque.append(node.right)
            else:
                res += 'X,'
        return res

    def deserilize(self, data):
        if not data:
            return TreeNode(None)
        data = data.split(',')
        root = TreeNode(data.pop(0))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if data:
                val = data.pop(0)
                if val != 'X':
                    node.left = TreeNode(val)
                    queue.append(node.left)
            if data:
                val = data.pop(0)
                if val != 'X':
                    node.right = TreeNode(val)
                    queue.append(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
