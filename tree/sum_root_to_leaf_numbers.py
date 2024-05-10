# Sum Root to Leaf Numbers

# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

 

# Example 1:
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.


# Example 2:
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def create_tree():
    head = TreeNode(4)
    head.left = TreeNode(9)
    head.right = TreeNode(0)
    head.left.left = TreeNode(5)
    head.left.right = TreeNode(1)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    return head


anss = [0]
def get_root_to_child_path(head):
    def util(node, path_arr, ans_arr):
        if node is None:
            return 
        
        path_arr.append(node.val)
        if node.left is None and node.right is None:
            st = ""
            for i in path_arr:
                st += str(i)
            anss[0] += int(st)
            ans_arr.append(path_arr[::])
            path_arr.pop()
            return
        util(node.left, path_arr, ans_arr)
        util(node.right, path_arr, ans_arr)
        path_arr.pop()
    ans_arr = []
    util(head, [], ans_arr)
    return ans_arr

tree = create_tree()
print(get_root_to_child_path(tree))
print(anss[0])