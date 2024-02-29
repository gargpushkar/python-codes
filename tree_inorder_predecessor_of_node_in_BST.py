# Inorder Predecessor of Node in BST
# The inorder predecessor of a node p is the node q that comes just before p in the binary tree's inorder traversal.

# Given the root node of a binary search tree and the node p, find the inorder predecessor of node p. If it does not exist, return null.
"""
This is the Node class definition

class Node:
	def __init__(self, data=0, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

"""
from typing import Optional
from collections import deque

class Node:
	pass

class Solution:
	def findPredecessor(self, root: Optional[Node], p: Optional[Node]) -> Optional[Node]:
		# add your logic here
		if not root:
			return root
		pred_node = None
		stack = deque()
		current_node = root
		while current_node or stack:
			if current_node:
				stack.append(current_node)
				current_node = current_node.left
			else:
				current_node = stack.pop()
				if current_node.data == p.data:
					return pred_node
				pred_node = current_node
				current_node = current_node.right
		return None

