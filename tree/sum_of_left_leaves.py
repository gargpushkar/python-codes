# https://leetcode.com/problems/sum-of-left-leaves/description/
# Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# Example 2:
# Input: root = [1]
# Output: 0


from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        arr = [0]
        def solve(root, direction):
            if not root:
                return 0
            if direction == "L" and not root.left and not root.right:
                arr[0] += root.val
            
            solve(root.left, "L")
            solve(root.right, "R")
        solve(root, "")
        return arr[0]