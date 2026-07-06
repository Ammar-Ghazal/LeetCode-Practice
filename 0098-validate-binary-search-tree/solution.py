# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, left, right):
            # Time Complexity: O(n), each node is visited once
            # Space Complexity: O(h), for recursion stack, where h is the height of the tree
            # best case, this is O(log(n)) for balanced tree, worst case is O(n), a linked list
            if not node:
                return True
            elif not (node.val > left and node.val < right):
                return False
            return (isValid(node.left, left, node.val) and isValid(node.right, node.val, right))
        
        return isValid(root, float("-inf"), float("inf"))
