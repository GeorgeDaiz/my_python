"""
2.两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        ret = head
        if not l1:
            return l2
        elif not l2:
            return l1

        while l1 and l2:
            add = l1.val + l2.val + carry
            ret.next = ListNode(add % 10)
            ret = ret.next
            carry = add // 10
            l1 = l1.next
            l2 = l2.next

        l = l1 if l1 else l2
        while l:
            add = l.val + carry
            ret.next = ListNode(add % 10)
            ret = ret.next
            carry = add // 10
            l = l.next

        if carry:
            ret.next = ListNode(carry)

        return head.next

    def add_two_numbers_re(self, l1: ListNode, l2: ListNode):
        if not l1 and not l2:
            return
        elif not(l1 and l2):
            return l1 or l2
        else:
            if l1.val + l2.val < 10:
                l3 = ListNode(l1.val + l2.val)
                l3.next = self.add_two_numbers_re(l1.next, l2.next)
            else:
                l3 = ListNode(l1.val + l2.val - 10)
                l3.next = self.add_two_numbers_re(l1.next, self.add_two_numbers_re(l2.next, ListNode(1)))
        return l3
