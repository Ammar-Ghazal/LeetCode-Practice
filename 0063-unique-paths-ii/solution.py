class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rowsize, colsize = len(obstacleGrid), len(obstacleGrid[0])
        paths = 0

        @cache
        def dfs(row, col):
            nonlocal paths
            if row >= rowsize or col >= colsize or obstacleGrid[row][col] == 1:
                return 0
            elif row == rowsize - 1 and col == colsize - 1:
                return 1
            return dfs(row + 1, col) + dfs(row, col + 1)

        return dfs(0, 0)
