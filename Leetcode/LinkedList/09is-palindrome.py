"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false

示例 2:

输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        if not head:
            return
        new = None
        while head:
            p = head
            head = head.next
            p.next = new
            new = p
        return new

    def is_palindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        new = self.reverse_list(slow)
        while new:
            if head.val != new.val:
                return False
            head = head.next
            new = new.next
        return True

