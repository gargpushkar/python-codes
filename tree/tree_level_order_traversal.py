# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if not root:
            return root

        ans = []
        q.append(root)
        while q:
            q_length = len(q)
            temp = []
            while q_length:
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                q_length -= 1
            if temp:
                ans.append(temp)
        return ans