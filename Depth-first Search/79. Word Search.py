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
#以下写法ok！增加了visited保存遍历状态 
#另外52&53两行的写法也很重要
#将dfs函数写在if条件里而非直接return dfs函数的结果，后者的错误是！！！会直接对[0][0]位置起始的判断结果return，找到就true 没找到就false，而非每个位置都遍历了以后确定trueorfalse
#也就是上面的两重for白写！就白写！！知道吗！！！
#这个代码写的还不够优雅 冗余 明天白天再抄一下答案的优雅写法 2020/10/25/00：34
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board,word,i,j,pos): #pos记录现在要满足word的第几个字母
            if pos==len(word):
                return True
            visited[i][j]=True
            if i>0 and not visited[i-1][j] and board[i-1][j]==word[pos] and dfs(board,word,i-1,j,pos+1):
                return True
            if i<row-1 and not visited[i+1][j] and board[i+1][j]==word[pos] and dfs(board,word,i+1,j,pos+1):
                return True
            if j>0 and not visited[i][j-1] and board[i][j-1]==word[pos] and dfs(board,word,i,j-1,pos+1):
                return True
            if j<col-1 and not visited[i][j+1] and board[i][j+1]==word[pos] and dfs(board,word,i,j+1,pos+1):
                return True
            visited[i][j]=False
            return False
        result=False
        row=len(board)
        col=len(board[0])
        visited=[[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0] and dfs(board,word,i,j,1):
                        result=True
        return result
