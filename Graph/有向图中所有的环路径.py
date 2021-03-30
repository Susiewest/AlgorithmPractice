# 用邻接表保存图+dfs
# 路径指的是，从起点到环入口
# graph = {1:[node1的邻居们],2:[], ……}
from copy import deepcopy
Class Solution():
  def __init__(self):
    #如果存在多个环，result要在递归中append多次, 所以定义在函数外
  	self.result = [] 
  
  def dfs(self, graph, route, current_node):
    route = deepcopy(route)
    if current_node in route: 
      # 如果当前节点已经在路径中，说明有环,
	    # 找到环起点在路径中的位置，打印这个位置之前的
      cycle_start = route.index(current_node)
      temp = [str[i] for i in route[:cycle_start+1]]
      self.result.append(''.join(temp))
      return
    route.append(current_node)
    for neighbour in graph[node]:
      self.dfs(graph, route, neighbour)

graph = {1:[2], 2:[3,4],3:[1]}
sol = Solution()
ans = sol.dfs(graph,[],1)
