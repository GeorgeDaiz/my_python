# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge_two_list(self, head1: ListNode, head2: ListNode) -> ListNode:
        p1 = head1
        p2 = head2
        if p1 and p2:
            if p1.val <= p2.val:
                head = p1
                p1 = p1.next
            else:
                head = p2
                p2 = p2.next
            r = head
        elif p1:
            return p1
        else:
            return p2
        while p1 and p2:
            if p1.val <= p2.val:
                r.next = p1
                p1 = p1.next
                r = r.next
            else:
                r.next = p2
                p2 = p2.next
                r = r.next
        if p1:
            r.next = p1
        elif p2:
            r.next = p2
        return head

    def merge_two_list_re(self, head1: ListNode, head2: ListNode) -> ListNode:
        merged = None
        if not head1:
            return head2
        elif not head2:
            return head1

        if head1.val <= head2.val:
            merged = head1
            head1 = head1.next
            merged = merged.next
        else:
            merged = head2
            head2 = head2.next
            merged = merged.next
        return merged
