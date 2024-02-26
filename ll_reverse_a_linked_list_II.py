# Reverse a Linked List II
# Given a linked list and two numbers left and right, reverse the nodes from position 'left' to position 'right'. Assume: left <= right.

# Example
# left: 2, right: 4
# Linked list: 1→5→7→13
# Result: 1→13→7→5
# left: 2, right: 3
# Linked list: 1→5→7→13
# Result: 1→7→5→13

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

def get_ll() -> ListNode:
    node1 = ListNode(1, None)
    node2 = ListNode(5, None)
    node3 = ListNode(7, None)
    node4 = ListNode(13, None)
    node5 = ListNode(27, None)
    # node6 = ListNode(41, None)
    # node7 = ListNode(7, None)
    # node8 = ListNode(18, None)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # node5.next = node6
    # node6.next = node7
    # node7.next = node8
	
    return head

head = get_ll()
def print_ll(head):
    while(head):
        print(head.data, end=" ")
        head = head.next
    print()

def reverse_ll(head, right, count):
    prev = None
    current_node = head
    # while current_node:
    while current_node and count <= right:
        temp = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = temp
        count += 1
    head.next = current_node
    return prev


left = 1
right = 2
current = head
count = 1
prev = None
while current and count < left:
      prev = current
      current = current.next
      count += 1

print_ll(head)
if prev == None: 
    head = reverse_ll(head, right, count)
else:
    prev.next = reverse_ll(prev.next, right, count) 
print_ll(head)
