"""
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的KthLargest类需要一个同时接收整数k 和整数数组nums的构造器，它包含数据流中的初始元素。每次调用KthLargest.add，返回当前数据流中第K大的元素。

示例:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3); // returns 4
kthLargest.add(5); // returns 5
kthLargest.add(10); // returns 5
kthLargest.add(9); // returns 8
kthLargest.add(4); // returns 8
说明:
你可以假设nums的长度≥k-1且k ≥1。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class KthLargest:
    def __init__(self, k: int, nums: list):
        self.k = k
        self.root = None
        self.size = 0
        for num in nums:
            self.root = self.insert_root(self.root, num)
            self.root = self.keep_k(self.root)

    def insert_root(self, root, num):
        if not root:
            self.size += 1
            return TreeNode(num)
        if root.val > num:
            root.left = self.insert_root(root.left, num)
        else:
            root.right = self.insert_root(root.right, num)
        return root

    def keep_k(self, root):
        if self.size <= self.k:
            return root
        if not root:
            return None
        elif root.left:
            root.left = self.keep_k(root.left)
        else:
            self.size -= 1
            if not (root.left or root.right):
                root = None
            else:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
        return root

    def successor(self, root):
        """
        One step right and then always left
        """
        # 后继节点
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        """
        One step left and then always right
        """
        # 前驱节点
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val == key:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def get_min(self):
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.val

    def add(self, val: int) -> int:
        self.root = self.insert_root(self.root, val)
        self.root = self.keep_k(self.root)
        return self.get_min()


from heapq import *


class KthLargest1(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = list(nums)
        self.nums.sort()
        if len(self.nums) > k:
            self.nums = self.nums[len(self.nums) - k:]
        heapify(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            heappush(self.nums, val)
            heapify(self.nums)
        else:
            top = self.nums[0] if len(self.nums) > 0 else float('-inf')
            if top < val:
                heapreplace(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
