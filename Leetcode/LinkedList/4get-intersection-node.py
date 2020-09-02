class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 找到两个单链表相交的起始节点
    @staticmethod
    def get_intersection_node(head1: ListNode, head2: ListNode):
        if not head1 or not head2:
            return
        l1 = head1
        l2 = head2
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
            if not l1 and not l2:
                return None
            if not l1:
                l1 = head1
            if not l2:
                l2 = head2
        return l1
