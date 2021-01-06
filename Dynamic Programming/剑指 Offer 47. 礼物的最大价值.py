class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
        #初始化第一行
        dp[0][0]=grid[0][0]
        for i in range(1,len(grid[0])):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        #初始化第一列
        for j in range(1,len(grid)):
            dp[j][0]=dp[j-1][0]+grid[j][0]
        for j in range(1,len(grid)):
            for i in range(1,len(grid[0])):
                dp[j][i]=max(dp[j-1][i],dp[j][i-1])+grid[j][i]
        return dp[-1][-1]
执行用时：60 ms, 在所有 Python3 提交中击败了40.39%的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了11.05%的用户

先初始化再dp比直接在双层循环里判断是否i==0/j==0再初始化，省去了冗余的判断
因为当行列足够大时，i==0/j==0的情况比较少，每次循环都判断会比较麻烦
此外不一定要另外开辟dp，直接在grid上写会降低空间复杂度

