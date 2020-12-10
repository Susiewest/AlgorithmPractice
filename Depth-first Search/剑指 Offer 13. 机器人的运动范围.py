写的dfs，也可以用队列实现，队列的话每次pop一个以后也是上下左右加一通。
有个自己写的bug处，就是set的初始化。想先把起点（0，0）加入，
如果这样写： visited = set((0,0)) 就会出错， visited={0}
可以这样写： 1.visited = set() visited.add((0,0))
也可以： visited = {(0,0}}
还有一个对所有位数之<=k的条件，比较聪明的写法 if sum(int(i) for i in str(new_x)+str(new_y))<=k
写法2 sum(map(int, str(x)+str(y))) > k   map返回迭代器
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        directions = {(1,0),(-1,0),(0,1),(0,-1)}
        visited = set() #起点直接加入
        visited.add((0,0))
        def dfs(visited, start_x, start_y):
            for direction in directions:
                ele_sum = 0
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                if 0<=new_x<m and 0<=new_y<n and (new_x,new_y) not in visited:
                    for i in range(len(str(new_x))):
                        ele_sum += int(str(new_x)[i])
                    for j in range(len(str(new_y))):
                        ele_sum += int(str(new_y)[j])
                    if ele_sum<=k:
                        visited.add((new_x,new_y))
                        dfs(visited, new_x, new_y)
        dfs(visited,0,0)
        return len(visited)

执行用时：72 ms, 在所有 Python3 提交中击败了39.29%的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了8.83%的用户
        
