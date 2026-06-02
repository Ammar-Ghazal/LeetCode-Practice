class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        maxA = min(height[0], height[1])
        l, r = 0, len(height) - 1

        while l < r:
            maxA = max(min(height[l], height[r]) * (r - l), maxA)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        
        return maxA

