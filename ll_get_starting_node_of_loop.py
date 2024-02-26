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
    
    def get_ll(self):
        return self.head
    
    def get_intersection_node(self, ll1, ll2):
        return True

        


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(2)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(7)
    # ll.remove_duplicates()