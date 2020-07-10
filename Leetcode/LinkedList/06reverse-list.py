# -*- coding:utf-8 -*-
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        if not head:
            return
        p = head
        q = head.next
        p.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        return p

    def reverse_list1(self, head: ListNode) -> ListNode:
        if not head:
            return
        new = None
        while head:
            p = head
            head = head.next
            p.next = new
            new = p
        return new

    def reverse_list_re(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        headNode = self.reverse_list_re(head.next)
        head.next.next = head
        head.next = None
        return headNode


if __name__ == '__main__':
    solution = Solution()
