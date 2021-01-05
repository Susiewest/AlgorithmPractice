#91题 0不对应任何字母，需要单独讨论当前字母为0/不为0/前一位字母为0/不为0
这题0对应a，不用讨论当前字母了，因为0也可以独立划分为一位。但前一位字母是否为0还需要讨论，尽管连续两位在0-25之间，但如果前一位为0，仍只能划分成一个结果，‘0’‘9’，而不能‘09’
class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        if len(num)<2:
            return 1
        dp = [0]*(len(num))
        dp[0]=1
        if 0<int(num[0:2])<=25:
            dp[1]=2
        else:
            dp[1]=1   
        for i in range(2,len(num)):
            if 0<int(num[i-1:i+1])<=25:
                if num[i-1]=='0':
                    dp[i]=dp[i-1]
                else:
                    dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]
        return dp[-1]
执行用时：32 ms, 在所有 Python3 提交中击败了93.33%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了18.03%的用户
