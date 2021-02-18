"""
23. 合并K个升序链表
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]

提示：
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 分治法
    def merge_two(self, head1: ListNode, head2: ListNode) -> ListNode:
        if not head1 or not head2:
            return head1 if not head2 else head2
        head = pre = ListNode(0)
        while head1 and head2:
            if head1.val <= head2.val:
                pre.next = head1
                head1 = head1.next
            else:
                pre.next = head2
                head2 = head2.next
            pre = pre.next
        pre.next = head1 if head1 else head2
        return head.next

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        elif l > r:
            return None
        mid = (l + r) // 2
        return self.merge_two(self.merge(lists, l, mid), self.merge(lists, mid+1, r))

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists)-1)
