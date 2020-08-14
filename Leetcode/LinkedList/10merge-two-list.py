"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def merge_two_list(head1: ListNode, head2: ListNode) -> ListNode:
        # 迭代
        p_head = ListNode(-1)
        prev = p_head
        while head1 and head2:
            if head1 < head2:
                prev.next = head1
                head1 = head1.next
            else:
                prev.next = head2
                head2 = head2.next
        prev.next = head1 if head1 else head2
        return p_head

    def merge_two_list_re(self, head1: ListNode, head2: ListNode) -> ListNode:
        # 递归
        if not head1:
            return head2
        elif not head2:
            return head1

        if head1.val <= head2.val:
            head1.next = self.merge_two_list_re(head1, head2)
            return head1
        else:
            head2.next = self.merge_two_list_re(head1, head2)
            return head2
