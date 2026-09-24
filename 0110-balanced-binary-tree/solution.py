# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # Time complexity: O(n)
            # Space complexity: O(h), h is logn best case, and h is n worst case
            if node is None: return (True, 0)
            left, right = dfs(node.left), dfs(node.right)

            balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            height = max(left[1], right[1]) + 1

            return (balanced, height)


        return dfs(root)[0]
