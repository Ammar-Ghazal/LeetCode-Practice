class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        heights = [0] * cols
        total = 0

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    heights[col] += 1
                else:
                    heights[col] = 0

            for right in range(cols):
                min_height = heights[right]

                for left in range(right, -1, -1):
                    min_height = min(min_height, heights[left])

                    if min_height == 0:
                        break

                    total += min_height

        return total
