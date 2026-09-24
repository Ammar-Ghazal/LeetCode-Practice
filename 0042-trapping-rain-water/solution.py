class Solution:
    def trap(self, height):
        # Time complexity: O(n)
        # Space complexity: O(1)
        size = len(height)
        left, right = 0, size - 1
        out, leftmax, rightmax = 0, 0, 0

        while left < right:
            # the idea is that we always want to process the shorter wall's side to ensure that
            # the shorter of the 2 walls can contain the water
            if height[left] < height[right]:
                leftmax = max(leftmax, height[left])
                out += leftmax - height[left]
                left += 1
            else:
                rightmax = max(rightmax, height[right])
                out += rightmax - height[right]
                right -= 1

        return out
