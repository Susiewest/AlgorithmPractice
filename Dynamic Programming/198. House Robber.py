class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        if len(nums)==1: return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]



'''执行用时：
48 ms, 在所有 Python3 提交中击败了20.19%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了76.19%的用户'''
