# Rotate a Linked List
# Given a linked list, rotate it to the right by k nodes.

# Examples:
# Input: 1→2→3→4
# k: 3
# Output: 2→3→4→1

# Input: 1→2→3
# k: 4
# Output: 3→1→2

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def print(self, node=None):
        if not node:
            node = self.head
        count = 0
        while node:
            print(node.data, end=" ")
            node = node.next
            count += 1
        print()
        print(count)
        return count

    def rotate(self, k):
        n = self.print()
        k = k%n
        if k == 0:
            self.print()
            return
        head_pos = n-k
        null_pos = n-k-1
        curr = self.head
        count = 0
        while curr:
            if count == null_pos:
                null = curr
            if count == head_pos:
                new_head = curr
            if count == n-1:
                last_node = curr
            curr = curr.next
            count += 1
        
        last_node.next = self.head
        null.next = None
        self.head = new_head
        self.print()

ll = LinkedList()
# ll.add_node(5)
# ll.add_node(4)
ll.add_node(3)
ll.add_node(2)
ll.add_node(1)
ll.rotate(1)