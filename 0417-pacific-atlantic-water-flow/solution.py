from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def bfs(starts, visit):
            q = deque(starts)
            for cell in starts:
                visit.add(cell)
            while q:
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS
                            and (nr, nc) not in visit
                            and heights[nr][nc] >= heights[r][c]):
                        visit.add((nr, nc))
                        q.append((nr, nc))

        pacStarts = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        atlStarts = [(ROWS - 1, c) for c in range(COLS)] + [(r, COLS - 1) for r in range(ROWS)]

        bfs(pacStarts, pac)
        bfs(atlStarts, atl)

        return [[r, c] for r in range(ROWS) for c in range(COLS)
                if (r, c) in pac and (r, c) in atl]
