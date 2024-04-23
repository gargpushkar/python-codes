# Reorder List

# Given a linked list of the form:

# N0 → N1 → N2 → ....Nn-2 → Nn-1
# Reorder the list in the following format:

# N0 → Nn-1 → N1 → Nn-2 → N2 → ....
# Example
# Linked list: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9
# Result: 1 → 9 → 2 → 8 → 3 → 7 → 4 → 6 → 5
# Linked list: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8
# Result: 1 → 8 → 2 → 7 → 3 → 6 → 4 → 5

"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""
class ListNode:
	pass

class Solution:
	
	def reverse_ll(self, node):
		prev = None
		curr = node
		while curr:
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp
		node = prev
		return prev
	
	def reorderList(self, head: ListNode) -> ListNode:
		# add your logic here
		if not head:
			return head
		slow = head
		fast = head.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		
		node1 = head
		node2 = slow.next
		slow.next = None
		node2 = self.reverse_ll(node2)
		
		node = ListNode(0)
		curr = node
		while node1 or node2:
			if node1:
				curr.next = node1
				curr = curr.next
				node1 = node1.next
			if node2:
				curr.next = node2
				curr = curr.next
				node2 = node2.next
		node = node.next
		return node
		


