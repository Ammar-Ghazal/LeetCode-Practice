class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time Complexity: O(m*n), where m is the number of rows, and n is the number of columns
        # Space Complexity: O(m*n), worst case for the max number of recursive calls
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
                
        return islands

