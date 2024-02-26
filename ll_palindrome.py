class Node:
    def __init__(self, data= 0, next= None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_node(self, data):
        if not self.head:
            node = Node(data)
            self.head = node
        else:
            current_node = self.head
            while(current_node.next):
                current_node = current_node.next
            node = Node(data)
            current_node.next = node
    
    def print_ll(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def check_palindrome(self):
        stack = []
        current_node = self.head
        while(current_node):
            stack.append(current_node.data)
            current_node = current_node.next
        current_node = self.head
        while(current_node):
            if current_node.data != stack.pop():
                return False
            current_node = current_node.next
        return True

    def merge_sorted_ll(self, firstList, secondList):
        if firstList.data < secondList.data:
            h = firstList
            while(firstList and secondList):
                while(firstList.next and firstList.next.data < secondList.data):
                    firstList = firstList.next
                temp = secondList.next
                secondList.next = firstList.next
                firstList.next = secondList
                secondList = temp
        else:
            h = secondList
            while(firstList and secondList):
                while(secondList.next and secondList.next.data < firstList.data):
                    secondList = secondList.next
                temp = firstList.next
                firstList.next = secondList.next
                secondList.next = firstList
                firstList = temp
        current_node = h
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def get_ll(self):
        return self.head


    def remove_duplicates(self):
        current_node = self.head
        prev_node = None
        while(current_node):
            if prev_node and current_node.data == prev_node.data:
                prev_node.next = current_node.next
            else:
                prev_node = current_node
            current_node = current_node.next
        
        self.print_ll()
        


if __name__ == "__main__":
    # ll = LinkedList()
    # ll.add_node(1)
    # ll.add_node(2)
    # ll.add_node(3)
    # ll1 = ll.get_ll()
    # firstList = ll.get_ll()

    # ll2 = LinkedList()
    # ll2.add_node(5)
    # ll2 = ll2.get_ll()
    # secondList = ll2
    # ll.merge_sorted_ll(ll1, ll2)
    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(2)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(7)
    ll.remove_duplicates()