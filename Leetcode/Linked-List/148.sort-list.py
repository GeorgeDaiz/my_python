"""
148. 排序链表
给你链表的头结点head，请将其按 升序 排列并返回 排序后的链表 。

进阶：
你可以在O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]

提示：
链表中节点的数目在范围[0, 5 * 104]内
-105<= Node.val <= 105
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 自顶向下归并排序
    def sort(self, head: ListNode, tail: ListNode):
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        slow = fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return self.merge(self.sort(head, mid), self.sort(mid, tail))

    def merge(self, head1, head2):
        temp_head = ListNode(0)
        temp, temp1, temp2 = temp_head, head1, head2
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        elif temp2:
            temp.next = temp2
        return temp_head.next

    def sortList(self, head: ListNode) -> ListNode:
        return self.sort(head, None)


class Solution1:
    def merge(self, head1, head2):
        temp_head = ListNode(0)
        temp, temp1, temp2 = temp_head, head1, head2
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        elif temp2:
            temp.next = temp2
        return temp_head.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        # 记录链表长度
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        temp_head = ListNode(0, head)
