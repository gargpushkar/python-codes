"""
This is the ListNode class definition
"""

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

def get_ll() -> ListNode:
    node1 = ListNode(1, None)
    node2 = ListNode(2, None)
    node3 = ListNode(3, None)
    node4 = ListNode(14, None)
    node5 = ListNode(5, None)
    node6 = ListNode(16, None)
    node7 = ListNode(7, None)
    node8 = ListNode(18, None)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
	
    return head

head = get_ll()
def print_ll(head):
    while(head):
        print(head.data, end=" ")
        head = head.next

print()
head = get_ll()

def print_in_reverse(head):
	if head.next:
		print_in_reverse(head.next)
	print(head.data, end=" ")

print_in_reverse(head)


print()
def reverse_l(head: ListNode):
    current_node = head
    prev = None
    while(current_node):
        print(current_node.data)
        next = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = next
    return prev

print()
print_ll(reverse_l(head))