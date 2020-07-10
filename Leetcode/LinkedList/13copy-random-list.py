"""
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

    val：一个表示 Node.val 的整数。
    random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # 遍历两次，将新旧链表对照关系存入hash_table中。先构建一个纯next的链表，之后再次循环就得到带random的链表
    @staticmethod
    def copy_random_list(head: 'Node') -> 'Node':
        node_dict = {}
        dummy = Node(0, None, None)
        node_dict[head] = dummy
        new_head = dummy
        pointer = head
        while pointer:
            node = Node(pointer.val, pointer.next, None)
            node_dict[pointer] = node
            new_head.next = node
            new_head, pointer = new_head.next, pointer.next
        pointer = head
        while pointer:
            if pointer.random:
                node_dict[pointer].random = node_dict[pointer.random]
            pointer = pointer.next
        return dummy.next
