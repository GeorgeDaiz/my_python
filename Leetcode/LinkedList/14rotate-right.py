"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def rotate_right(head: ListNode, k: int):
        if not head:
            return
        if k == 0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        count = 0
        p = dummy
        while p.next:
            p = p.next
            count += 1
        if count < 2 or k % count == 0:
            return head
        p.next = dummy.next
        for _ in range(count - k % count):
            p = p.next
        head = p.next
        p.next = None
        return head

    @staticmethod
    def rotate_right1(head: ListNode, k: int):
        # 将首尾相连，构造成循环链表；
        # 根据k算出有效步数，从中间断开即可
        p = head
        count = 1  # 记录链表长度

        if not head:
            return []

        # 首尾相连，并记录链表长度
        while p.next:
            p = p.next
            count += 1
        p.next = head

        p = head
        # 有效步数
        step = count - k % count - 1
        for _ in range(step):
            p = p.next
        head = p.next
        p.next = None

        return head
