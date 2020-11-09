使用bfs的方法就是拓扑排序判断有没有环 使用dfs的方法就是使用记忆数组
拓扑排序（bfs）法：1. 初始化邻接表 入度表 统计入度/邻接填入list 
2. 队列中加入所有初始入度为0的节点
3. 只要队列不为空，出队一个入度为0的节点，记录处理完的节点数（加入结果集/numcourses-1），将所有邻接点（它指向的节点）的入度-1，如果-1后入度为0，加入队列
4. 当队列为空的时候，检查结果集中的顶点个数是否和课程数相等/numcourses==0？即可

import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #使用bfs的方法就是拓扑排序判断有没有环 使用dfs的方法就是使用记忆数组
        adjacent = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        queue = collections.deque()
        for cur, pre in prerequisites:
            indegrees[cur]+=1
            adjacent[pre].append(cur)
        for i in range(numCourses):
            if not indegrees[i]: #首先加入所有入度为0的节点
                queue.append(i)
        while queue:
            cur = queue.popleft()
            numCourses-=1
            for course in adjacent[cur]:
                #邻接点入度-1
                indegrees[course]-=1
                #入度为0了再加入queue
                if not indegrees[course]:
                    queue.append(course)
        return numCourses==0

执行用时：44 ms, 在所有 Python3 提交中击败了93.66%的用户
内存消耗：14.2 MB, 在所有 Python3 提交中击败了52.12%的用户

dfs判断有无环
#使用bfs的方法就是拓扑排序判断有没有环 使用dfs的方法就是使用记忆数组
#flag=0 未被访问 flag=1 之前访问过，返回，flag=2，当前点访问过程中遇到过，成环，return false，这里是只要有一个false就是false，所以记得把dfs写在if里，而非return dfs

import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(adjacent, flag, i):
            if flag[i]==1:
                return True
            if flag[i]==2:
                return False
            flag[i]=2
            for j in adjacent[i]:
                if not dfs(adjacent, flag, j):
                    return False
            #记得让flag变为1 以后对于别的节点来说 它是之前遍历过的 可以直接返回结果true 而非当前环中遍历过
            flag[i]=1
            return True
        #使用bfs的方法就是拓扑排序判断有没有环 使用dfs的方法就是使用记忆数组
        flag = [0 for _ in range(numCourses)]
        adjacent = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacent[pre].append(cur)
        for i in range(numCourses):
            if not dfs(adjacent, flag, i):
                return False
        return True
        
执行用时：56 ms, 在所有 Python3 提交中击败了46.52%的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了19.96%的用户
