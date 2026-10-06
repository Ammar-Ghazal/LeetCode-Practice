class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rowLen, colLen = len(board), len(board[0])
        visited = set() # necessary to avoid backwards pathing, if word was ABA and we only had AB, it can return true if it goes back to the only A, when it should return False

        def dfs(row, col, remWord):
            if remWord == "": return True
            elif row < 0 or col < 0 or row >= rowLen or col >= colLen: return False
            elif (row, col) in visited: return False
            elif remWord[0] != board[row][col]: return False

            visited.add((row, col))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dirRow, dirCol in directions:
                if dfs(row+dirRow, col+dirCol, remWord[1:]):
                    visited.remove((row, col)) # why is this here
                    return True
            visited.remove((row, col)) # no idea why this is here
            return False # why is this here
        
        for i in range(rowLen):
            for j in range(colLen):
                if word[0] == board[i][j]:
                    if dfs(i, j, word):
                        return True
    
        return False
