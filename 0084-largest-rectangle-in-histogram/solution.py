class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] # (index, height) -> use stack to store both index and the height

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height: # if the stack exists, and the height is greater than the height we just reached, pop it from the stack
                popi, popheight = stack.pop() # the popped index and height values
                maxArea = max(maxArea, popheight * (i - popi))
                start = popi
            stack.append((start, height))

        # compute the remaining heights (rectangles that extend all the way to the end of the histogram):
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea
