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
