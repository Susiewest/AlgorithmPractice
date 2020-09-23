#https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
「动态规划」的一个关键的步骤是想清楚「状态如何转移」。事实上，「回文」天然具有「状态转移」性质。

一个回文去掉两头以后，剩下的部分依然是回文（这里暂不讨论边界情况）；
依然从回文串的定义展开讨论：

如果一个字符串的头尾两个字符都不相等，那么这个字符串一定不是回文串；
如果一个字符串的头尾两个字符相等，才有必要继续判断下去。
如果里面的子串是回文，整体就是回文串；
如果里面的子串不是回文串，整体就不是回文串。
即：在头尾字符相等的情况下，里面子串的回文性质据定了整个子串的回文性质，这就是状态转移。因此可以把「状态」定义为原字符串的一个子串是否为回文子串。

边界条件是：表达式 [i + 1, j - 1] 不构成区间，即长度严格小于 2，即 j - 1 - (i + 1) + 1 < 2 ，整理得 j - i < 3。
只要一得到 dp[i][j] = true，就记录子串的长度和起始位置，没有必要截取，这是因为截取字符串也要消耗性能，记录此时的回文子串的「起始位置」和「回文长度」即可。


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        dp=[[False for _ in range(len(s))]for _ in range(len(s))]
        #dp = [[False] * len(s) for _ in range(len(s))] 这个写法也是ok滴
        start, maxlen=0, 1
        for i in range(len(s)):
            dp[i][i]=True
        #无敌重要！！！为什么先j后i 因为这个填表顺序很重要 我们需要先知[i+1][j-1]位置的true false才能填当前位置，画一下表格会发现 需要按竖着的方向填
        #不然就会出现需要调用表格里的填空 还没填进去正确的值
        for j in range(1,len(s)):
            for i in range(j):
                if s[i]==s[j]:
                    if j-i<3:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]       
                if dp[i][j] and j-i+1>maxlen:
                    maxlen=j-i+1
                    start=i
        #return s[start,start+maxlen]
        return s[start:start+maxlen]

'''执行用时：
4288 ms, 在所有 Python3 提交中击败了47.64%的用户
内存消耗：
21.8 MB, 在所有 Python3 提交中击败了6.48%的用户'''


#中心扩散法 定义的函数既能解决偶数个 也能解决奇数
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)-1):
            left1, right1=self.expand(s,i,i)
            left2, right2=self.expand(s,i,i+1)
            if right1-left1>end-start:
                start=left1
                end=right1
            if right2-left2>end-start:
            #elif right2-left2>end-start: 不是非你即我的关系 是都要比的关系
                start=left2
                end=right2
        return s[start:end+1]

        
    def expand(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left=left-1
            right=right+1
        return left+1, right-1
   
'''执行用时：
1024 ms, 在所有 Python3 提交中击败了81.23%的用户
内存消耗：
13.3 MB, 在所有 Python3 提交中击败了85.86%的用户'''
