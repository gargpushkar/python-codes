# Reverse a Linked List in k-groups
# Given a linked list and a positive number k, reverse the nodes in groups of k.

# All the remaining nodes after multiples of k should be left as it is.

# Example
# k: 3
# Linked list: 1→2→3→4→5→6→7→8→9
# Result: 3→2→1→6→5→4→9→8→7
# k: 3
# Linked list: 1→2→3→4→5→6→7→8
# Result: 3→2→1→6→5→4→7→8
# Note: Solve using O(1) extra space.

class Node:
    def __init__(self, data=0, next=None) -> None:
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
        return count

    def reverse_in_k(self, k):
        def reverse(head, k, length):
            # Base Case
            if head is None or length < k or k == 1 or head.next is None:
                return head
            # reverse k nodes
            prev = None
            curr = head
            next = None
            count = 0
            while curr and count < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count += 1
            
            if next:
                head.next = reverse(next, k, length - k)

            return prev
        length = self.print()
        self.head = reverse(self.head, k, length)


    
ll = LinkedList()
ll.add_node(6)
ll.add_node(5)
ll.add_node(4)
ll.add_node(3)
ll.add_node(2)
ll.add_node(1)
# ll.print()
ll.reverse_in_k(9)
ll.print()