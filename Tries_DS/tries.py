# Tries 

class TrieNode:
    def __init__(self) -> None:
        self.count = 0
        self.children = [None for _ in range(26)]


def insert_word(root, key):
    current_node = root
    for c in key:
        if not current_node.children[ord(c) - ord('a')]:
            current_node.children[ord(c) - ord('a')] = TrieNode()
        current_node = current_node.children[ord(c) - ord('a')]
    current_node.count += 1

def search_word(root, key):
    current_node = root
    for c in key:
        if not current_node.children[ord(c) - ord('a')]:
            return False
        current_node = current_node.children[ord(c) - ord('a')]
    
    return current_node.count > 0


root = TrieNode()

insert_word(root, "hello")
insert_word(root, "hell")
insert_word(root, "push")
insert_word(root, "pushkar")

print(search_word(root, "helloo"))