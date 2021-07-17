感觉这个题其实跟编辑距离是一个思路，先判断当前位置的word1，word2相不相等，然后去基于二维数组里的左、上、左上 去取合适的值，
不同的是 如果word1[i] == word2[j] 编辑距离是之前的dp，而在这个题，最长公共子序列是dp+1.

0行0列代表着两个空字符串之间的对比，0行代表一个字符串为空，0列代表另一个字符串为空
也就是dp[i][j]代表的是字符串0-(i-1)和0-(j-1)之间的最大公共子序列
https://leetcode-cn.com/problems/longest-common-subsequence/solution/fu-xue-ming-zhu-er-wei-dong-tai-gui-hua-r5ez6/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row, col = len(text1), len(text2)
        dp = [[0]*(col+1) for _ in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
执行用时：520 ms, 在所有 Python3 提交中击败了13.60%的用户
内存消耗：22.4 MB, 在所有 Python3 提交中击败了69.35%的用户

