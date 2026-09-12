class Solution:
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        ogColor = image[sr][sc]

        if ogColor == newColor:
            return image
        
        def dfs(r, c):
            if image[r][c] == ogColor:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r - 1, c)
                if r < R - 1:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c < C - 1:
                    dfs(r, c + 1)
            
        dfs(sr, sc)
        return image


        # if original == color:
        #     return image

        # image[sr][sc] = color

        # if sr >= 1:
        #     if image[sr - 1][sc] == original:
        #         self.floodFill(image, sr - 1, sc, color)

        # if sr < len(image) - 1:
        #     if image[sr + 1][sc] == original:
        #         self.floodFill(image, sr + 1, sc, color)

        # if sc >= 1:
        #     if image[sr][sc - 1] == original:
        #         self.floodFill(image, sr, sc - 1, color)

        # if sc < len(image[0]) - 1:
        #     if image[sr][sc + 1] == original:
        #         self.floodFill(image, sr, sc + 1, color)

        # return image
