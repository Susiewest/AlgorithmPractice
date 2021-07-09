#感觉和200题有点像诶
先从四条边出发，有O的都改成新字符B，dfs覆盖
这样最后剩下的O都改成X，B恢复成O
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row=len(board)
        col=len(board[0])
        def dfs(i,j):
            board[i][j]='B'
            for direction in {(1,0),(-1,0),(0,1),(0,-1)}:
                new_x=i+direction[0]
                new_y=j+direction[1]
                if 0<=new_x<row and 0<=new_y<col and board[new_x][new_y]=='O':
                    dfs(new_x,new_y)
        for i in range(row):
            if board[i][0]=='O':
                dfs(i,0)    
            if board[i][col-1]=='O' :
                dfs(i,col-1)       
        for j in range(col):
            if board[0][j]=='O':
                dfs(0,j)
            if board[row-1][j]=='O':
                dfs(row-1,j)
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='B':
                    board[i][j]='O'
                    
执行用时：60 ms, 在所有 Python3 提交中击败了43.96%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了25.34%的用户

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(board, x, y, row, col):
            board[x][y]='B'
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0<=new_x<row and 0<=new_y<col:
                    if board[new_x][new_y]=='O':
                        dfs(board, new_x, new_y, row, col)
        row = len(board)
        col = len(board[0])
        for i in range(row):
            if board[i][0]=='O':
                dfs(board, i, 0, row, col)
            if board[i][col-1]=='O':
                dfs(board, i, col-1, row, col)
        for j in range(col):
            if board[0][j]=='O':
                dfs(board, 0, j, row, col)
            if board[row-1][j]=='O':
                dfs(board, row-1, j, row, col)
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='B':
                    board[i][j]='O'
        return board


执行用时：40 ms, 在所有 Python3 提交中击败了99.11%的用户
内存消耗：18.7 MB, 在所有 Python3 提交中击败了69.50%的用户

