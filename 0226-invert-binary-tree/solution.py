# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time Complexity: O(n), n is number of nodes
        # Space Complexity: O(h) -> number of recursive call stacks needed, O(n) worst case, and O(log(n)) best case

        # base case: dont do or return anything
        if not root:
            return None
        
        # swap the two children:
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # call the function on the two children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
