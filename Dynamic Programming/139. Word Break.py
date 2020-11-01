39/43 首先初始化错误不应该break 其次 双层循环范围错误 第三 不适用dp[0] 也就是dp[1]代表第一个字符是否在worddict里 会更方便
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #我的定义方式 dp[i]表示 s[0]到s[i]是否在worddict里 也就是字符串前i+1位是否满足
        #dp[j]=dp[i]+s[i,j] in worddict 
        #这样写一个很大的问题 dp[i]的i和i，j的i，重叠了一位
        #如果改为dp[j]=dp[i]+s[i+1,j] in worddict 那么j也取不到 dp[j]代表的是[0:j] 含义不一致 无法形成完整区间
        #再改为dp[j]=dp[i]+s[i+1,j+1] in worddict 
        #将dp[i]的含义改为 表示s[0:i] 也就是i取不到 比较合适 也就是字符串前i位是否满足
        #总结：将dp[i]的含义 从s[0]到s[i]改为s[0:i]
        if not wordDict:
            return False
        length=len(s)
        dp=[False for _ in range(length)]
        initial=0
        for i in range(length):
            if s[:i+1] in wordDict:
                initial=i
                dp[initial]=True
                break
        if not dp[initial]:
            return False
        for j in range(initial,length):
            for k in range(j+1,length):
                if dp[j] and s[j+1:k+1] in wordDict:
                    dp[k]=True
        return dp[-1]

AC
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
        length=len(s)
        dp=[False for _ in range(length+1)]
        dp[0]=True #空字符为true 这只是为了让边界情况也能满足状态转移方程，即：当前半部分为空字符串时， dp[i+1] 全然取决于[0,i]子串是否为一个单词表单词，所以让 dp[0] = true
        for i in range(length):
            for j in range(i+1,length+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j]=True
        return dp[-1]
执行用时：44 ms, 在所有 Python3 提交中击败了89.78%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了11.23%的用户

超时了 抄了一句@functools.lru_cache(）就通过了
functools.lru_cache的作用主要是用来做缓存，他能把相对耗时的函数结果进行保存，避免传入相同的参数重复计算。同时，缓存并不会无限增长，不用的缓存会被释放。
相当于自动加了个结果词典，计算过的分支直接调用结果

import functools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @functools.lru_cache(None)
        def canbreak(s:str):
            if not s:
                return True
            for i in range(1,len(s)+1):
                if s[:i] in wordDict and canbreak(s[i:]):
                    return True
            return False
        return canbreak(s)
执行用时：52 ms, 在所有 Python3 提交中击败了63.46%的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了5.17%的用户

因为觉得functools很trick所以想自己实现出来保存重复计算这一步，但是一直超时，难过，提交通过率又低了
但是ac的那一刻 呜呜呜眼眶热了 只要努力！！！就有好事发生！！！加油！！！
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo=defaultdict()
        def canbreak(s:str):
            if not s:
                return True
            if s in memo.keys():
                return memo[s]           
            for i in range(1,len(s)+1):
                if s[:i] in wordDict and canbreak(s[i:]):
                    memo[s]=True
                    return True
            memo[s]=False #忘了写这里所以还是没能加速很多 写上就ac了
            return False
        return canbreak(s)
        
执行用时：40 ms, 在所有 Python3 提交中击败了96.02%的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了5.17%的用户
