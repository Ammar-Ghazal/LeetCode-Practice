class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time Complexity: O(m*n), where m is the number of rows, and n is the number of columns
        # Space Complexity: O(m*n), worst case for the max number of recursive calls
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        cols, rows = len(grid), len(grid[0])
        islands = 0

        def dfs(col, row):
            if col < 0 or row < 0 or col >= cols or row >= rows or grid[col][row] == "0":
                return
            grid[col][row] = "0"
            for c, r in directions:
                dfs(col + c, row + r)
            return
        

        for c in range(cols):
            for r in range(rows):
                if grid[c][r] == "1":
                    dfs(c, r)
                    islands += 1
        
        return islands

