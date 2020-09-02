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
