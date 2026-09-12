# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time complexity: O(h), h = log(n) best, h = n worst
        # Space Complexity: O(1)
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val: # go right subtree
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val: # go left subtree
                curr = curr.left
            else: # nodes split and curr is LCA, or p/q is the curr node and also LCA
                return curr
