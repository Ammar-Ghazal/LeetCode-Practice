# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time complexity: O(n)
        # Space complexity: O(n)
        if root is None:
            return []

        queue = deque([root])
        out = []

        while queue:
            levelSize = len(queue)
            levelNodes = []

            for _ in range(levelSize):
                cur = queue.popleft()
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                levelNodes.append(cur.val)
            
            out.append(levelNodes)

        return out
