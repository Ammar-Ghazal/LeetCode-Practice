# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorderValToIndex = {val: idx for idx, val in enumerate(inorder)}
        preorder_index = 0

        def build(leftBound, rightBound):
            nonlocal preorder_index

            if leftBound > rightBound:
                return None

            root = TreeNode(preorder[preorder_index])
            preorder_index += 1

            mid = inorderValToIndex[root.val]

            root.left = build(leftBound, mid - 1)
            root.right = build(mid + 1, rightBound)

            return root

        return build(0, len(inorder) - 1)




        # Time complexity: O(n^2) worst case in skewed tree, O(nlogn) in balanced tree
        # Space complexity: O(n^2) worst case, O(n) best case -> both exclude the returned tree which needs O(n)
        # if not preorder or not inorder: return None

        # root = TreeNode(preorder[0]) # root is always first value in preorder array
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root
         
