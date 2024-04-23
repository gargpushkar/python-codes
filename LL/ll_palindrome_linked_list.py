# Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

class ListNode:
    def __init__(self, data = 0, next = None) -> None:
        self.data = data
        self.next = next

def get_ll() -> ListNode:
    node1 = ListNode(1, None)
    node2 = ListNode(2, None)
    node3 = ListNode(3, None)
    node4 = ListNode(14, None)
    node5 = ListNode(14, None)
    node6 = ListNode(3, None)
    node7 = ListNode(2, None)
    node8 = ListNode(1, None)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    return head

def print_ll(node):
    count = 0
    while node:
        print(node.data, end=" ")
        node = node.next
        count += 1
    return count

ll = get_ll()
# leng = print_ll(ll)

def reverse_ll(node):
    prev_node = None
    while node:
        next_node = node.next
        node.next = prev_node
        prev_node = node
        node = next_node
    return prev_node

slow = ll
fast = ll.next
count = 1
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    count += 2
slow.next = reverse_ll(slow.next)
# print(count)

# print(slow.data)
print_ll(ll)


def isPalindrome(node) -> bool:
    slow = node
    fast = node.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow = slow.next
    while slow:
        if slow.data != node.data:
            return False
        slow = slow.next
        node = node.next
    return True

print(isPalindrome(ll))