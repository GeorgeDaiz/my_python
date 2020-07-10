class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def print_from_tail_to_head(self):
        array = []
        while ListNode:
            array.append(ListNode.val)
            ListNode = ListNode.next
        return array[::-1]
