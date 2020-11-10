和207题的区别在于，207只需要判断能不能学完所有课，这个题需要给出学习的路径来。
依然使用拓扑排序，区别在于每次popleft的时候把pop出来的课程（入度已经为0）加入result列表中
最后bfs结束了，看看result列表中是不是所有的课？不是 就学不完 return[] 是 就return result

1、在开始排序前，扫描对应的存储空间（使用邻接表），将入度为0 的结点放入队列。

2、只要队列非空，就从队首取出入度为 0 的结点，将这个结点输出到结果集中，并且将这个结点的所有邻接结点（它指向的结点）的入度减1，在减 1以后，如果这个被减1的结点的入度为 0 ，就继续入队。

3、当队列为空的时候，检查结果集中的顶点个数是否和课程数相等即可。

需要两个辅助的数据结构：

1、邻接表：通过结点的索引，我们能够得到这个结点的后继结点；

2、入度数组：通过结点的索引，我们能够得到指向这个结点的结点个数。

如果使用dfs，就需要改成逆邻接表，也就是记录每个节点的前驱节点，当所有的前驱节点遍历输出完了以后才能输出当前节点。
当访问一个结点的时候，应当先递归访问它的前驱结点，直至前驱结点没有前驱结点为止。

import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacent = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        result = []
        for cur, pre in prerequisites:
            adjacent[pre].append(cur)
            indegrees[cur]+=1
        queue = collections.deque()
        for i in range(numCourses):
            if indegrees[i]==0:
                queue.append(i)
        while queue:
            cur = queue.popleft()
            result.append(cur)
            for next_node in adjacent[cur]:
                indegrees[next_node]-=1
                if indegrees[next_node]==0:
                    queue.append(next_node)
        return result if len(result)==numCourses else []
        
执行用时：52 ms, 在所有 Python3 提交中击败了64.76%的用户
内存消耗：14.3 MB, 在所有 Python3 提交中击败了48.65%的用户

