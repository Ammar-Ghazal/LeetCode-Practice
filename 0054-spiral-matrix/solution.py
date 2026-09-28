class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row, col = len(matrix), len(matrix[0])
        direction = 1 # start by going right and down
        i, j = 0, -1
        output = []

        while row * col > 0:
            # move horizontally
            for _ in range(col):
                j += direction
                output.append(matrix[i][j])
            row -= 1
            for _ in range(row):
                i += direction
                output.append(matrix[i][j])
            col -= 1
            direction *= -1
        
        return output


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         row, col = len(matrix), len(matrix[0]) # Initial possible number of steps
#         direction = 1 # Start off going right
#         i, j = 0, -1
#         output = []
#         while row*col > 0:
#             for _ in range(col): # move horizontally
#                 j += direction
#                 output.append(matrix[i][j])
#             row-= 1
#             for _ in range(row): # move vertically
#                 i += direction
#                 output.append(matrix[i][j])
#             col-=1
#             direction *= -1 # flip direction
#         return output
