class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(n*m)
        # Space Complexity: O(n*m)
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set() # sets for pacific and atlantic oceans to keep track, and to avoid duplicates

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
                r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                    return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            # run dfs on first row cells = 0, pacific ocean rows
            dfs(0, c, pac, heights[0][c])

            # run dfs on last row, atlantic ocean
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            # run dfs on first col cells, pacific oean
            dfs(r, 0, pac, heights[r][0])
            
            # run dfs on last col cels, atlantic ocean
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])

        return result
