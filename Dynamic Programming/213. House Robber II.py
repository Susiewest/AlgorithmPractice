class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        def dynamicCalculate(new_nums):
            n = len(new_nums)
            dp = [0]*(n+1)
            # dp[i]前i个屋子可偷的最大金额
            dp[1] = new_nums[0]
            for i in range(2,n+1):
                # 第i间屋子不偷/偷
                dp[i] = max(dp[i-1], dp[i-2]+new_nums[i-1])
            return dp[-1]
        result = max(dynamicCalculate(nums[:-1]), dynamicCalculate(nums[1:]))
        return result
执行用时：48 ms, 在所有 Python3 提交中击败了14.55%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了8.10%的用户

