"""
This is the Node class definition


"""
from typing import Optional


class Node:
	def __init__(self, data=0, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

class Solution:
	
	def is_mirror(self, root1, root2):
		if root1 is None and root2 is None:
			return True
		""" For two trees to be mirror images, 
            the following three conditions must be true
            1 - Their root node's key must be same
            2 - left subtree of left tree and right subtree
            of the right tree have to be mirror images
            3 - right subtree of left tree and left subtree
            of right tree have to be mirror images
        """
		if root1 is not None and root2 is not None:
			if root1.data == root2.data:
				return self.is_mirror(root1.left, root2.right) and self.is_mirror(root1.right, root2.left)
		return False
	
	def isSymmetric(self, root: Optional[Node]) -> bool:
		# add your logic here
		 return self.is_mirror(root, root)


