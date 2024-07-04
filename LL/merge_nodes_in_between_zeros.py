# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp_head = head
        prev_zero_node = head
        total = 0
        while head:
            if head.val == 0:
                prev_zero_node.val = total
                if not head.next:
                    prev_zero_node.next = None
                    return temp_head.next
                prev_zero_node = prev_zero_node.next
                total = 0
            total += head.val
            head = head.next
