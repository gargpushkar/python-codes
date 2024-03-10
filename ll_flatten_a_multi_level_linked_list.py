# https://workat.tech/problem-solving/practice/flatten-multi-level-linked-list
# Flatten a Multi-Level Linked List
# You are given a linked list structure, where each node has two pointers:

# next: points to an identical node towards the right.
# down: points to an identical node towards the bottom.
# Only the top most node can have a non-NULL next pointer.

# This gives us a set of vertical linked lists and a horizontal linked list with the head nodes of the vertical lists.

# Also, all vertical lists are sorted.

# Your task is to flatten the lists into a single linked list, which should also be sorted.

import heapq

class ListNode:
    def __init__(self, data=0, next=None, down=None) -> None:
        self.data = data
        self.next = next
        self.down = down

def create_ll():
    node1 = ListNode(1)
    node5 = ListNode(5)
    node8 = ListNode(8)
    node13 = ListNode(13)

    node1.next = node5
    node5.next = node8
    node8.next = node13

    node1.down = ListNode(3)
    node1.down.down = ListNode(8)

    node5.down = ListNode(8)

    node8.down = ListNode(14)
    node8.down.down = ListNode(26)

    node13.down = ListNode(15)
    node13.down.down = ListNode(22)
    node13.down.down.down = ListNode(25)

    return node1

head = create_ll()
def traverse_ll(node):
    curr = node
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def down_traverse(node):
    curr = node
    while curr:
        print(curr.data, end=" ")
        curr = curr.down
    print()
# traverse_ll(head)
# down_traverse(head)
# down_traverse(head.next)
# down_traverse(head.next.next)
# down_traverse(head.next.next.next)

minHeap = []

curr = head
hash_map = {}
i=0
while curr:
    heapq.heappush(minHeap, [curr.data, i])
    hash_map[i] = curr.down
    i+=1
    curr=curr.next

current_node = ListNode()
ans_head = current_node

while minHeap:
    data, indx = heapq.heappop(minHeap)
    current_node.next = ListNode(data)
    current_node = current_node.next
    if hash_map[indx]:
        heapq.heappush(minHeap, [hash_map[indx].data, indx])
        hash_map[indx] = hash_map[indx].down

traverse_ll(ans_head.next)
