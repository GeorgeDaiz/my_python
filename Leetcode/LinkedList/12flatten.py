"""
You are given a doubly linked list which in addition to the next and previous pointers,
it could have a child pointer, which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure,
as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# DFS
class Solution:
    def flatten(self, head: Node):
        if not head:
            return
        node = head
        while node:
            if node.child:
                flattened = self.flatten(node.child)
                node.child = None
                next_node = self.append_to_list(node, flattened)
                node = next_node
            else:
                node = node.next
        return head

    @staticmethod
    def append_to_list(node: Node, flattened: Node) -> Node:
        next_node = node.next
        node.next = flattened
        flattened.prev = node
        while node.next:
            node = node.next
        node.next = next_node
        if next_node:
            next_node.prev = node
        return next_node
