"""
This is the ListNode class definition
"""

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next



class Solution:
	def addTwoNumbers(self, firstList: ListNode, secondList: ListNode) -> ListNode:
		# add your logic here
		C = None
		carry = 0
		while(firstList or secondList):
			temp_node = ListNode()
			if firstList and secondList:
				if carry:
					temp_sum = firstList.data + secondList.data + carry
					carry = 0 
				else:
					temp_sum = firstList.data + secondList.data
				if temp_sum >= 10:
					carry = 1
					temp_node.data = temp_sum - 10
				else:
					temp_node.data = temp_sum
				firstList = firstList.next
				secondList = secondList.next
			elif firstList:
				if carry:
					temp_sum = firstList.data + carry
					carry = 0 
				else:
					temp_sum = firstList.data
				if temp_sum >= 10:
					carry = 1
					temp_node.data = temp_sum - 10
				else:
					temp_node.data = temp_sum
				firstList = firstList.next
			elif secondList:
				if carry:
					temp_sum = secondList.data + carry
					carry = 0 
				else:
					temp_sum = secondList.data
				if temp_sum >= 10:
					carry = 1
					temp_node.data = temp_sum - 10
				else:
					temp_node.data = temp_sum
				secondList = secondList.next
			if not C:
				C = temp_node
				C_head = C
			else:
				C.next = temp_node
				C = C.next
		if carry:
			temp_node = ListNode(carry)
			C.next = temp_node
			C = C.next
		return C_head
	


	
	
	def print_ll(self, ll):
		while(ll):
			print(ll.data)
			ll = ll.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)


sol = Solution()
sol.addTwoNumbers(l1, l2)