from ll import LinkedList

l1 = LinkedList()
l1.add_node(9)
# l1.add_node(4)
# l1.add_node(5)
# l1.add_node(4)
l1.print_ll()

print("")

l2 = LinkedList()
l2.add_node(3)
l2.add_node(9)
# l2.add_node(1)
l2.print_ll()


def add_ll(l1, l2):
    l3 = LinkedList()
    carry = 0
    while(l1 or l2):
        if l1 and l2:
            if carry:
                temp_sum = l1.data + l2.data + carry
                carry = 0
            else:
                temp_sum = l1.data + l2.data + carry
            if temp_sum >= 10:
                carry = 1
                temp_sum = temp_sum - 10
            l3.add_node(temp_sum)
            l1 = l1.next
            l2 = l2.next
        elif l1:
            if carry:
                temp_sum = l1.data + carry
                carry = 0
            else:
                temp_sum = l1.data + carry
            if temp_sum >= 10:
                carry = 1
                temp_sum = temp_sum - 10
            l3.add_node(temp_sum)
            l1 = l1.next
        elif l2:
            if carry:
                temp_sum = l2.data + carry
                carry = 0
            else:
                temp_sum = l2.data + carry
            if temp_sum >= 10:
                carry = 1
                temp_sum = temp_sum - 10
            l3.add_node(temp_sum)
            l2 = l2.next
    if carry:
        l3.add_node(1)
    # if l1:
    #     while(l1):
    #         l3.add_node(l1.data)
    #         l1 = l1.next
    # if l2:
    #     while(l2):
    #         l3.add_node(l2.data)
    #         l2 = l2.next
    l3.print_ll()
    return l3.get_ll()

print(" ")
add_ll(l1.get_ll(), l2.get_ll())

        