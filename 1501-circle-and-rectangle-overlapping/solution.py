class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Time complexity: O(1)
        # Space complexity: O(1)

        # The below 2 lines of code determine the point on the rectangle that is closest to the circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        dx = xCenter - closest_x
        dy = yCenter - closest_y

        return dx ** 2 + dy ** 2 <= radius ** 2
