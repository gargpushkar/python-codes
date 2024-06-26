# Balance a Binary Search Tree
# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        

        def create_balanced_bst(arr):
            if not arr:
                return
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left = create_balanced_bst(arr[:mid])
            root.right = create_balanced_bst(arr[mid+1:])
            return root
        return create_balanced_bst(arr)
        
