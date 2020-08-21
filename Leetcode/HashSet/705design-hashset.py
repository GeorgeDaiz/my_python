"""
设计哈希集合
不使用任何内建的哈希表库设计一个哈希集合

具体地说，你的设计应该包含以下的功能

add(value)：向哈希集合中插入一个值。
contains(value) ：返回哈希集合中是否存在这个值。
remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

示例:
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1); // 返回 true
hashSet.contains(3); // 返回 false (未找到)
hashSet.add(2);
hashSet.contains(2); // 返回 true
hashSet.remove(2);
hashSet.contains(2); // 返回  false (已经被删除)

注意：
所有的值都在[0, 1000000]的范围内。
操作的总数目在[1, 10000]范围内。
不要使用内建的哈希集合库。
"""


class Node:
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, new):
        if not self.exists(new):
            new_node = Node(new, self.head.next)
            self.head.next = new_node

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.val == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        return False


class MyHashSet:
    # 单独链表法处理冲突
    # hash_key空间设为质数769
    # 使用链表来存储所有值，插入和删除时间复杂度都是O(1)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_range = 769
        self.bucket_array = [Bucket() for i in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range

    def add(self, key: int) -> None:
        bucket_idx = self._hash(key)
        self.bucket_array[bucket_idx].insert(key)

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        self.bucket_array[bucket_idx].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket_idx = self._hash(key)
        return self.bucket_array[bucket_idx].exists(key)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
