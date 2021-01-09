动态规划，设置三个指针指向第一个丑数，每个丑数都是之前的某个丑数*2或者3或者5
在各种可能的拼接相乘里选择最小的一个，选完了这个数*2/3/5就不能再选了
没想明白 明天再说 888

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]*n
        a, b, c = 0, 0, 0
        for i in range(1,n):
            n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(n2,n3,n5)
            if dp[i]==n2: a+=1
            if dp[i]==n3: b+=1
            if dp[i]==n5: c+=1
        return dp[-1]
执行用时：128 ms, 在所有 Python3 提交中击败了93.72%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了19.08%的用户
