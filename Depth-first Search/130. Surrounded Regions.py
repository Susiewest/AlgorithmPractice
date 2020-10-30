#感觉和200题有点像诶
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
