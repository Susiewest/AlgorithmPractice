import numpy as np
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
        board_padding = np.array([[0 for _ in range(col+2)] for _ in range(row+2)])
        board_padding[1:row+1, 1:col+1] = board
        for i in range(1,row+1):
            for j in range(1,col+1):
                temp_sum = np.sum(board_padding[i-1:i+2,j-1:j+2]*kernel)
                if board_padding[i][j]==1:
                    if temp_sum<2 or temp_sum>3:
                        board[i-1][j-1] = 0
                    if temp_sum==2 or temp_sum==3:
                        board[i-1][j-1] = 1
                else:
                    if temp_sum==3:
                        board[i-1][j-1] = 1
        return board


执行用时：96 ms, 在所有 Python3 提交中击败了7.93%的用户
内存消耗：28.8 MB, 在所有 Python3 提交中击败了5.01%的用户

