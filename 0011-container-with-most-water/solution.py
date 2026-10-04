class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Time complexity: O(n)
        # Space complexity: O(1)
        maxA = 0
        l, r = 0, len(height) - 1

        while l < r:
            leftHeight, rightHeight = height[l], height[r]
            if leftHeight > rightHeight:
                maxA = max(maxA, rightHeight * (r - l))
                r -= 1
            else:
                maxA = max(maxA, leftHeight * (r - l))
                l += 1
        
        return maxA
