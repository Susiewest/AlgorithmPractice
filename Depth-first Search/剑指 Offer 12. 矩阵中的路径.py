和79题同
#这个题目要注意的，一个是把函数放在if的条件里，保证有一个true就每层都return true，不要写在if下面，这样第一个是false就直接return了
#第二点 要设置visited，因为四个方向试探的时候不能试探已经遍历过的
#第三点 终止条件
#第四点 pos的初始值到底是0还是1
#第五点！！！！！ if 0<=new_x<row and 0<=new_y<col and not visited[new_x][new_y] and dfs(board, new_x, new_y,directions, visited, pos+1):
不要写成
if 0<=new_x<row and 0<=new_y<col and dfs(board, new_x, new_y,directions, visited, pos+1) and not visited[new_x][new_y]:
先判断未访问过再dfs的顺序很重要！！！ 如果先dfs，会把访问过的newx，newy，标记为访问过，在退出dfs函数的时候，会恢复为未访问过，这样就满足了not visited，其实是不满足的！会出错啊啊啊啊啊啊啊

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        row = len(board)
        col = len(board[0])
        visited = [[False]*col for _ in range(row)]
        def dfs(board, start_x, start_y, directions, visited, pos):
            #终止条件一开始写pos==len，returnTrue，但其实第len个位置，不需要要求startx starty，也就是上一层循环的new_x,new_y在限制范围内。像for循环里的if条件，只需执行到最后一个pos，而非最后一个再后面一个的pos。
            if pos == len(word)-1:
                return board[start_x][start_y]==word[-1]
            if board[start_x][start_y]==word[pos]:
                visited[start_x][start_y]=True
                for direction in directions:
                    new_x = start_x+direction[0]
                    new_y = start_y+direction[1]
                    if 0<=new_x<row and 0<=new_y<col and not visited[new_x][new_y] and dfs(board, new_x, new_y,directions, visited, pos+1):
                        return True
                visited[start_x][start_y]=False
            return False

        for i in range(row):
            for j in range(col):
                if dfs(board,i,j,directions, visited, 0):
                    return True
        return False
执行用时：196 ms, 在所有 Python3 提交中击败了92.22%的用户
内存消耗：14.5 MB, 在所有 Python3 提交中击败了71.96%的用户
        
