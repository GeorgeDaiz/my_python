"""
给定一个链表，删除链表的倒数第n个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
    @staticmethod
    def remove_nth_from_end(head: ListNode, n: int) -> ListNode:

        fast, slow = head, head
        while n:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
