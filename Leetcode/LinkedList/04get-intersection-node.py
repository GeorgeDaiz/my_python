class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 找到两个单链表相交的起始节点
    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        l1 = headA
        l2 = headB
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
            if not l1 and not l2:
                return None
            if not l1:
                l1 = headB
            if not l2:
                l2 = headA
        return l1
