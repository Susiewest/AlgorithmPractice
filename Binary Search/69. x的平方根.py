#牛顿法
class Solution:
    def mySqrt(self, x: int) -> int:
        #f(x)-f(x0)=f'(x)(x-x0) 
        #f(x)=0 x=x0-f(x0)/f'(x)
        #f(x)=x^2-a when a=题目给的x 解函数里的x x从1开始找（从几都行）
        #x=x0-(x0^2-a)/(2x0)=(x0/2)+a/(2x0)
        if x==0:
            return 0
        x_0=1
        pre=0
        while(abs(pre-x_0)>=1e-6):
            pre=x_0
            x_0=x_0/2+x/(2*x_0)
        return int(x_0)

'''执行结果：
通过
执行用时：
44 ms, 在所有 Python3 提交中击败了84.16%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了6.06%的用户'''
