# Lowest Common Ancestor in Binary Tree
# The lowest common ancestor of two nodes p and q is the lowest node in the binary tree that has p and q as its descendants.
# Note: A node is also considered a descendant of itself.

# Given the reference to the root node and two nodes p and q in a binary tree, return the reference to the lowest common ancestor of p and q.

# Note: You can assume that p and q will be present in the tree.

from typing import Optional

class Node:
	def __init__(self, data=0, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


class Solution:
	def path_to_node(self, node, path, key):
		if node is None:
			return False
		path.append(node)
		if node.data == key:
			return True
		if ((node.left and self.path_to_node(node.left, path, key)) or (node.right and self.path_to_node(node.right, path, key))):
			return True
		
		path.pop()
		return False
	
	def lowestCommonAncestor(self, root: Node, p: Node, q: Node) -> Optional[Node]:
		# add your logic here
		path1 = []
		path2 = []
		root1 = root
		root2 = root
		self.path_to_node(root1, path1, p.data)
		self.path_to_node(root2, path2, q.data)
		i = 0
		while i < len(path1) and i < len(path2):
			if path1[i].data != path2[i].data:
				break
			i+=1
		return path1[i-1]


root = Node(1)
root.left = Node(2)
# root.right = Node(3)
root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
root.left.left.left = Node(5)
root.left.left.left = Node(6)
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.left.left.left = Node(8)

sol = Solution()
print(sol.lowestCommonAncestor(root, root.left, root.left.left.left).data)