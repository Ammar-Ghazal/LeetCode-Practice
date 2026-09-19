class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # Time complexity: O(rxc)
        # Space Complexity: O(rxc)
        rotten = deque() # keeps track of newly/initially rotten oranges
        healthy, minutes = 0, 0 # minutes is output, healthy is # of normal oranges left
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] # valid directions to go, no diagonals

        # first, see where all rotten oranges are, and count number of healthy oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    healthy += 1

        while rotten and healthy:
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                for r, c in directions:
                    rdir = row + r
                    cdir = col + c
                    if (rdir < 0) or (rdir >= rows) or (cdir < 0) or (cdir >= cols):
                        continue
                    elif grid[rdir][cdir] == 1:
                        rotten.append((rdir, cdir))
                        healthy -= 1
                        grid[rdir][cdir] = 2
            minutes += 1

        
        return minutes if healthy == 0 else -1
