#超时 502个测试用例过了500个
class Solution:
    def trailingZeroes(self, n: int) -> int:
        multi_result=1
        for i in range(1,n+1):
            multi_result*=i
        multi_result=str(multi_result)
        reback=1
        count=0
        #while(!multi_result[-reback])
        while(multi_result[-reback]=='0'):
            count+=1
            reback+=1
        return count
        
        
#日了 这样写更超时 统计尾数中0的个数 不再转字符串后统计 而是判断对10取余能否=0
class Solution:
    def trailingZeroes(self, n: int) -> int:
        multi_result=1
        for i in range(1,n+1):
            multi_result*=i
        count=0
        while(multi_result%10==0):
            count+=1
            #multi_result/=10 这样除得到的是float
            multi_result//=10
        return count
        
        
#拆分阶乘会发现 2的个数比5的个数多 因此每个5必定能分配一个2
#只需统计5的个数 就是0的个数
#5的个数 每五个数有一个 每25个数（5*5）有两个 每125个数（5*5*5）有三个
#25里有一个5被整除5计数了 125里有两个5被计数了
#因此只需统计n中有多少个5+有多少个25+有多少个125。。。
#为了不超时 换一种方法 统计25/125...转变为 n每次//5，统计整除后的数中5的个数 即25的个数 125的个数。。
#https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/xiang-xi-tong-su-de-si-lu-fen-xi-by-windliang-3/
#这个讲解不错
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        while(n):
            if n//5:
                count+=n//5
            n//=5
        return count
        
        
        
 '''执行用时：
28 ms, 在所有 Python3 提交中击败了99.55%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了81.72%的用户'''
