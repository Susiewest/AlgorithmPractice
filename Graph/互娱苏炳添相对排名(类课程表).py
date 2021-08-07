import collections
num = int(input())
for i in range(num):
    data = input().split(' ')
    N, M = int(data[0]), int(data[1])
    # rank = dict()
    # # 初始化rank字典，key是排名，value是list，期望每个list长度为1，如果不为1 则存在不确定的因素
    # for j in range(N):
    #     rank[j] = []
    adjacent = [[] for _ in range(N)]
    indegrees = [0 for _ in range(N)]
    result = []
    flag = False
    for k in range(M):
        each_person = input().split(' ')[1:]
        each_person = [int (r) for r in each_person]
        for i in range(len(each_person)-1):
            adjacent[each_person[i]-1].append(each_person[i+1]-1)
            indegrees[each_person[i+1]-1] += 1
    if indegrees.count(0) > 1:
        print('NO')
        flag = True
        continue
    queue = collections.deque()
    for j in range(N):
        if indegrees[j] == 0:
            queue.append(j)
            indegrees[j]-=1
    while queue:
        cur = queue.popleft()
        result.append(cur)
        for next_node in adjacent[cur]:
            indegrees[next_node] -= 1
        if indegrees.count(0) > 1:
            print('NO')
            flag = True
            break
        if indegrees[next_node] == 0:
            queue.append(next_node)
            indegrees[next_node] -= 1

    if flag:
        continue
    if len(result) == N:
        # 将0~N-1恢复为运动员编号1~N
        for i in range(N):
            result[i] = str(result[i]+1)
        result = ' '.join(result)
        print(result)
    else:
        print('NO')
        # # 第一个人的记忆直接存进去
        # if len(rank[0])==0:
        #     for index, item in enumerate(each_person):
        #         rank[index].append(item)
        # else:
        #     for item in each_person:
        #         if item in rank[]
        #         rank[index].append(item)
        #
        # for key, value in rank.items():
        #     if len(value)>1:





