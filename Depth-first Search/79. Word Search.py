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
    
'''执行用时：
116 ms, 在所有 Python3 提交中击败了97.09%的用户
内存消耗：
15.1 MB, 在所有 Python3 提交中击败了8.78%的用户'''

#看了答案默写都能出错 偶服辣
#dfs内：终止条件-当前状态改变-判断新位置是否越界-调用递归-递归结束后状态恢复方便后续遍历
#易错点：
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(board,word,row,col,start_x,start_y,visited,pos): #pos记录现在要满足word的第几个字母
            if pos==len(word): #出错位置2
                return True
            if board[start_x][start_y]==word[pos]:
                visited[start_x][start_y]=True
                for direction in directions:
                    new_x=start_x+direction[0]
                    new_y=start_y+direction[1]
                    if 0<=new_x<row and 0<=new_y<col and not visited[new_x][new_y]:
                        dfs(board,word,row,col,new_x,new_y,visited,pos+1) #出错位置1
                visited[start_x][start_y]=False
            return False
        result=False
        row=len(board)
        col=len(board[0])
        visited=[[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if dfs(board,word,row,col,i,j,visited,0):
                        result=True
        return result

#dfs内：终止条件-当前状态改变-判断新位置是否越界-调用递归-递归结束后状态恢复方便后续遍历
#易错点：1. 只要有一个是true就true 这个思想的表达方式
#2. 终止条件 一开始写的是处理到word后一个空字符（？）时结束 return true 
#这样会对测试用例[[a]]报错，因为newx，newy会越界，根本不会执行下一层循环再满足if pos==len：return true
#所以在处理最后一个字符的时候就要终止了
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(board,word,row,col,start_x,start_y,visited,pos): #pos记录现在要满足word的第几个字母
            if pos==len(word)-1:
                return board[start_x][start_y]==word[pos]
            if board[start_x][start_y]==word[pos]:
                visited[start_x][start_y]=True
                for direction in directions:
                    new_x=start_x+direction[0]
                    new_y=start_y+direction[1]
                    if 0<=new_x<row and 0<=new_y<col and not visited[new_x][new_y] and dfs(board,word,row,col,new_x,new_y,visited,pos+1):
                        return True
                visited[start_x][start_y]=False
            return False
        result=False
        row=len(board)
        col=len(board[0])
        visited=[[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if dfs(board,word,row,col,i,j,visited,0):
                        result=True
        return result
'''执行用时：
188 ms, 在所有 Python3 提交中击败了92.09%的用户
内存消耗：
14.7 MB, 在所有 Python3 提交中击败了25.03%的用户'''
