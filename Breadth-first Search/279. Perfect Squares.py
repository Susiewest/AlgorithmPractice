动态规划的方法
问题：为什么转移方程不采用dp[i]=dp[i-j]+dp[j]
我的分析：
导致的问题1. dp[i]=dp[i-j*j]+1初始化所有dp[i]为i 如果dp[i]=dp[i-j]+dp[j]仍采纳这个初始化，大家不会有任何更新，永远维持原样
那么需要更改初始化，不能赋最差的值为初始化，而是要给出开头几个位置确定的值，根据之前确定的值来计算后续的值，但这样又会导致一个问题，那就是j的取值范围是从1到i-1，
那么每个i的计算都要从前往后做遍历和计算，很费时间，如果是dp[i]=dp[i-j*j]+1，需要做尝试的j就很少，只有根号下i次即可

导致的问题2. j的取值范围是从1到i-1，j取不到i
dp（81）=dp（81-j的平方）+1 j可以取到9 而dp（81）=dp（81-j）+dp（j），j取不到81 无法找到最优解1，而是找到81=8*8+4*4+1*1

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(n+1):
            for j in range(i):
                if j*j>i:
                    break
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]

执行用时：5468 ms, 在所有 Python3 提交中击败了25.34%的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了37.23%的用户


BFS的方法：以n为根节点，构造子节点（n-1的平方） （n-2的平方）... 对（n-1的平方）所在层的所有节点继续往下构建，直到遇到第一个0，return所在的层数，即0节点的最小深度
原来用这个方法根本不用构造树，bfs为什么要构造父子节点之间的关系？只是为了遍历到父节点的时候可以方便找到子节点入队列，
而这道题根本不需要通过节点之间的边来定位找到子节点，只需要计算数字就可以找到下一层节点。
所以不需要建立父子节点间的关系，只需记录当前层的点和下层算出的新点即可，用两个set分别保存，用list也可以，但set的话不用重复计算相同数字的向下扩展～


class Solution:
    def numSquares(self, n: int) -> int:
        queue = {n}
        level = 0
        square_nums = [i*i for i in range(1, int(math.sqrt(n))+1)]
        while queue:
            level+=1
            next_queue = set()  #这个的位置很重要，必须是等遍历完当前的queue后才重置，而非当前层每个cur重置一次
            for cur in queue:
                for square in square_nums:
                    if cur-square==0:
                        return level
                    elif square>cur:
                        break
                    elif square<cur:
                        next_queue.add(cur-square)
            queue = next_queue

执行用时：244 ms, 在所有 Python3 提交中击败了83.82%的用户
内存消耗：14.5 MB, 在所有 Python3 提交中击败了14.18%的用户

