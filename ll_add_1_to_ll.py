from ll import LinkedList

class ListNode:
    def __init__(self, data= 0, next= None):
        self.data = data
        self.next = next

l1 = LinkedList()
l1.add_node(9)
l1.add_node(9)
l1.add_node(9)
l1.print_ll()

print("")


def reverse_ll(l):
    prev = None
    while(l):
        temp = l.next
        l.next = prev
        prev = l
        l = temp
    return prev

def addOneToList(self, head: ListNode) -> ListNode:
    prev = None
    while(l1):
        temp = l1.next
        l1.next = prev
        prev = l1
        l1 = temp
    
    carry = 0
    add_1 = 1
    prev_head = prev
    while(prev):
        temp_sum = prev.data + add_1 + carry
        add_1 = 0
        if temp_sum >= 10:
            carry = 1
            prev.data = temp_sum - 10
        else:
            carry = 0
            prev.data = temp_sum
        if not prev.next and carry:
            prev.next = ListNode(carry)
            break
        prev = prev.next
    if carry:
        temp_node = ListNode(carry)
        prev = temp_node

    prev = None
    while(prev_head):
        temp = prev_head.next
        prev_head.next = prev
        prev = prev_head
        prev_head = temp

    return prev

print(" ")
print(add_1_ll(l1.get_ll()))

        