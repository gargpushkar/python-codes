# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/?envType=daily-question&envId=2024-07-05

# A critical point in a linked list is defined as either a local maxima or a local minima.
# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].



from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            return [-1, -1]
        min_dist, max_dist = float('inf'), float('-inf')
        counter = 1
        prev_val = head.val
        head = head.next
        first_critical_point = None
        prev_critical_point = None
        while head and head.next:
            if prev_val < head.val > head.next.val or prev_val > head.val < head.next.val:
                if not first_critical_point:
                    first_critical_point = counter
                else:
                    max_dist = max(max_dist, counter - first_critical_point)
                    min_dist = min(min_dist, counter - prev_critical_point)
                prev_critical_point = counter
                
            counter += 1
            prev_val = head.val
            head = head.next
        if min_dist == float('inf') or max_dist == float("-inf"):
            return [-1, -1]
        return [min_dist, max_dist]