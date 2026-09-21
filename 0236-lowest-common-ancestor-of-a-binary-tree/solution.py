# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         if root is None:
#             return None
        
#         left_res = self.lowestCommonAncestor(root.left, p, q)
#         right_res = self.lowestCommonAncestor(root.right, p, q)
        
#         if (left_res and right_res) or (root in [p, q]):
#             return root
#         else:
#             return left_res or right_res

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right        
