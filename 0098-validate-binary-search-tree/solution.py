# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(h) -> height for number of recursive calls, log(n) best case, n worst case
        def dfs(node, left, right):
            if node is None:
                return True
            elif (node.val >= right) or (node.val <= left):
                return False
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        
        return dfs(root, float('-inf'), float('inf'))
