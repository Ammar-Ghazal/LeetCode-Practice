# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # Time complexity: O(n), traverses all nodes once
        # Space complexity: O(h), for call stack
        def dfs(node, depth):
            if node is None: return
            elif depth == len(output):
                output.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        output = []
        dfs(root, 0)
        return output

