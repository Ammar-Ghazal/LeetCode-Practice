class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # Time complexity: O(n)
        # Space complexity: O(h), O(logn) best case, O(n) worst case
        if root is None or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left or right
