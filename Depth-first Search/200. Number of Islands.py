from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        height = len(grid)
        width = len(grid[0])
        count = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j]=='1':
                    count+=1
                    self.grid_dfs(grid,i,j,height,width)
        return count
    def grid_dfs(self,grid,i,j,height,width):
        grid[i][j]='0'
        if i-1>=0 and grid[i-1][j]=='1': #上方
            self.grid_dfs(grid,i-1,j,height,width)
        if i+1<height and grid[i+1][j]=='1':#下方
            self.grid_dfs(grid,i+1,j,height,width)
        if j-1>=0 and grid[i][j-1]=='1': #左方
            self.grid_dfs(grid,i,j-1,height,width)
        if j+1<width and grid[i][j+1]=='1': #右方
            self.grid_dfs(grid,i,j+1,height,width)

sol=Solution()
result=sol.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
print(result)



'''执行用时：
56 ms, 在所有 Python3 提交中击败了99.55%的用户
内存消耗：
14.4 MB, 在所有 Python3 提交中击败了61.18%的用户'''

'''有人让我思考这个题在10wx10w格子的极端情况 dfs和bfs实现的差别 我感觉是bfs在空间复杂度上更优
但是对方说二者的时间空间应该都是一致的 我持保留态度 
说dfs是递归 递归的本质是栈 如果在10wx10w全是1的情况 会对所有格子都调用一次递归 都占用栈 而bfs不会'''
