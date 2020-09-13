#power of two原来是二次幂的意思 呆滞。。。
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        while(n%2==0):
            n=n/2
        return True if n==1 else False
'''执行用时：
40 ms, 在所有 Python3 提交中击败了84.64%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了62.12%的用户'''        
        

#惭愧 只能想到最笨的o(logn)的做法 下面的方法抄的题解区 位运算真是我永远也探测不透的操作
#https://leetcode-cn.com/problems/power-of-two/solution/power-of-two-er-jin-zhi-ji-jian-by-jyd/
#n为2的多少次幂 那么n&(n-1)必定为0
#我感觉这种位运算题是不是可以多写几个总结规律之类的。。。
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

'''执行用时：
52 ms, 在所有 Python3 提交中击败了18.94%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了66.36%的用户'''
