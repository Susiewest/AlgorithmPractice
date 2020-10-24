#以下写法是错误的 对false和true的return有问题
#还有很重要的一点，没有考虑状态，来时的路不能再参与遍历，若这次false了，来时的路又要恢复可以遍历
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board,word,i,j,pos): #pos记录现在要满足word的第几个字母
            if pos==len(word):
                return True
            if i>0 and board[i-1][j]==word[pos]:
                dfs(board,word,i-1,j,pos+1)
            if i<row-1 and board[i+1][j]==word[pos]:
                dfs(board,word,i+1,j,pos+1)
            if j>0 and board[i][j-1]==word[pos]:
                dfs(board,word,i,j-1,pos+1)
            if j<col-1 and board[i][j+1]==word[pos]:
                dfs(board,word,i,j+1,pos+1)
            return False
        result=False
        row=len(board)
        col=len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0] and dfs(board,word,i,j,1):
                        result=True
        return result
