#244 / 268 个通过测试用例
#"2101" 输出3 预期1
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s=='0': return 0
        dp=[None]*(len(s))
        dp[0]=1
        #啊呀！len==2的时候，不一定有两种呀，dp[1]也要分类讨论的   
        if len(s)>1:
            if s[1]=='0': 
                if 0<int(s[0:2])<=26: #10
                    dp[1]=dp[0]
                else: #30
                    return 0
            else: 
                if int(s[0:2])<=26:   #25 
                    dp[1]=2
                else:  #27
                    dp[1]=dp[0]
        else: #一位字符
            return 1
        for i in range(2,len(s)): 
            if s[i]=='0': 
                if 0<int(s[i-1:i+1])<=26: #xxx10/xxx20
                    dp[i]=dp[i-2]
                else:
                    return 0
            else:
                if int(s[i-1:i+1])<=26:
                    dp[i]=dp[i-1]+dp[i-2]
                else: #xxx27
                    dp[i]=dp[i-1]
        return dp[-1]

#终于ac了 反例1:"2101" 输出3 预期1 反例2:"01" 输出2 预期0
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s=='0': return 0
        dp=[None]*(len(s))
        dp[0]=1
        #啊呀！len==2的时候，不一定有两种呀，dp[1]也要分类讨论的   
        if len(s)>1:
            if s[1]=='0': 
                if 0<int(s[0:2])<=26: #10
                    dp[1]=dp[0]
                else: #30
                    return 0
            else:#这里改了
                if s[0]=='0':
                    return 0
                else:
                    if int(s[0:2])<=26:   #25 
                        dp[1]=2
                    else:  #27
                        dp[1]=dp[0]
        else: #一位字符
            return 1
        for i in range(2,len(s)): 
            if s[i]=='0': 
                if 0<int(s[i-1:i+1])<=26: #xxx10/xxx20 考虑00
                    dp[i]=dp[i-2]
                else:
                    return 0
            else:#这里也改了
                if s[i-1]=='0':  #xxxx09 9只能单独表示
                    dp[i]=dp[i-1]
                else:
                    if int(s[i-1:i+1])<=26: #不用考虑00
                        dp[i]=dp[i-1]+dp[i-2]
                    else: #xxx27
                        dp[i]=dp[i-1]
        return dp[-1]
        
执行用时：40 ms, 在所有 Python3 提交中击败了80.81%的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了26.03%的用户


