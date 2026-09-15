class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        curHeight = 0
        size = len(heights)
        out = deque()

        for i in range(size-1, -1, -1):
            if heights[i] > curHeight:
                curHeight = heights[i]
                out.appendleft(i)
        
        return list(out)
