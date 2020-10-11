#就不会做啊 结果是忽略了一个条件
#Only the filled cells need to be validated according to the mentioned rules.
#不用管有没有解 只要已经填了的ok就ok
#行列box分别搞9个字典 不同字典分离hash计数
#一次遍历 遍的时候直接确认box里的情况

#下面这个写法有点问题的
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[{} for _ in range(9)]
        col=[{} for _ in range(9)]
        box=[{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num=int(board[i][j])
                    box_index=(i//3)*3+j//3
                    row[i][num]=row[i].get(num,0)+1
                    col[j][num]=col[j].get(num,0)+1
                    box[box_index][num]=box[box_index].get(num,0)+1
                    #下面这句缩进没写对 和上一个if并列了 如果不执行上一个if 就不会有num
                if row[i][num]>1 or col[j][num]>1 or box_index[box_index][num]>1:
                    return False
        return True
        

#改进的地方 1. num转int不要写在if前 会报'.'转不了int的错
#2. 第二个if嵌套在第一个if里面 写外面和第一个并列会导致 row[i][.]没有key值 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[{} for _ in range(9)]
        col=[{} for _ in range(9)]
        box=[{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if board[i][j]!='.':  
                    num=int(num)     
                    box_index=(i//3)*3+j//3
                    row[i][num]=row[i].get(num,0)+1
                    col[j][num]=col[j].get(num,0)+1
                    box[box_index][num]=box[box_index].get(num,0)+1
                    #一开始下面这句缩紧没写对 和上一个if并列了 如果不执行上一个if 就不会有num
                    if row[i][num]>1 or col[j][num]>1 or box[box_index][num]>1:
                        return False
        return True
        
'''执行用时：
56 ms, 在所有 Python3 提交中击败了56.02%的用户
内存消耗：
13.4 MB, 在所有 Python3 提交中击败了51.15%的用户'''
