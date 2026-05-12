# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time Complexity: O(n) -> worst case in unbalanced tree
        # Space Complexity: O(h) -> h (height of tree) is n in the worst case, for the recursive call stack
        
        # if it is a leaf node, return None/Null
        if root == None:
            return

        # swap the two children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # call the invert function on the 2 subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # needed for leetcode grading
        return root

