class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<2:
            return False
        total = sum(nums)
        if total&1 or total>>1<max(nums): #sum是奇数
            return False
        target = total>>1
        dp = [[False]*(target+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1,n):
            for j in range(1,target+1):
                if j>=nums[i]:
                    dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n-1][target]
执行用时：2148 ms, 在所有 Python3 提交中击败了45.70%的用户
内存消耗：29.8 MB, 在所有 Python3 提交中击败了29.38%的用户

dp的优化做法，因为只需要前一行和当前行，所以空间上可以优化为两行。
这里更甚，可以直接在本行操作，更新本行。关键！因为dp[j] = dp[j] or dp[j-nums[i]]，这里dp[j-nums[i]]指的是上一行的状态，需要从后往前更新，不然前面先更新，后面就不能取到旧值了。
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<2:
            return False
        total = sum(nums)
        if total&1 or total>>1<max(nums): #sum是奇数
            return False
        target = total>>1
        dp=[True]+[False]*target
        for i in range(n):
            for j in range(target,nums[i]-1,-1): #犯错点 j-nums越界，那么就小于0以后就不更新了，保留dp[i-1][j]
                dp[j] = dp[j] or dp[j-nums[i]]
        return dp[-1]
执行用时：900 ms, 在所有 Python3 提交中击败了85.04%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了74.93%的用户


失败的硬币找零的bfs做法，322题硬币找零，每个面额是无限的，这里每个只有一次，就算每次选中以后remove掉，但是并不能保证当前道路是最优解，后面的选项不能基于remove后的做，无解了。。。除非回溯上层吧
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<2:
            return False
        total = sum(nums)
        if total&1 or total>>1<max(nums): #sum是奇数
            return False
        target = total>>1
        nums.sort()
        last = [target]
        current = []
        while(last):
            for i in last:
                for j in nums:
                    if i-j>0:
                        current.append(i-j)
                        nums.remove(j)
                    elif i-j==0:
                        return True
                    else:
                        break
            last = current
            current = []
        return False
