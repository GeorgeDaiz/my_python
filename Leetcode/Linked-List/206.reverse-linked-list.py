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
    @staticmethod
    def reverse_list(head: ListNode):
        if not head:
            return
        p = head
        q = None
        while p:
            r = p.next  # 暂存后继节点
            q.next = q  # 修改next引用指向
            q = p       # q暂存p
            p = r       # p访问下一节点
        return q

    @staticmethod
    def reverse_list_re(head: ListNode):
        def recur(cur, pre):
            if not cur:
                return pre              # 终止条件
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre              # 修改节点引用指向
            return res                  # 返回反转链表的头节点

        return recur(head, None)        # 调用递归并返回
