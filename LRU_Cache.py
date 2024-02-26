# https://workat.tech/problem-solving/practice/lru-cache
# LRU Cache
# Implement Least Recently Used (LRU) cache.

# You need to implement the following for the LRUCache class:

# LRUCache(int capacity) initializes the cache to store data of size: capacity.
# int get(int key) returns the value of the key if it exists, otherwise returns -1.
# void add(int key, int value) updates the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# Note: Try to achieve each operation in O(1) time complexity.

class DLL:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.hash_map = {}
        self.capacity = capacity
        self.head = DLL(0, 0)
        self.tail = DLL(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
    
    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_to_head(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
    
    def get(self, key):
        if key in self.hash_map:
            node = self.hash_map[key]
            value = node.value
            self.delete_node(node)
            self.add_to_head(node)
            return value

    def add(self, key, value):
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self.delete_node(node)
            self.add_to_head(node)
        else:
            node = DLL(key, value)
            self.hash_map[key] = node
            if self.count < self.capacity:
                self.count += 1
                self.add_to_head(node)
            else:
                del self.hash_map[self.tail.prev.key]
                self.delete_node(self.tail.prev)
                self.add_to_head(node)
