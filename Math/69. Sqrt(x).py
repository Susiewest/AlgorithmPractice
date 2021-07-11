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

class Solution:
    def mySqrt(self, x: int) -> int:
        # y = x^2 - c， c是待平方根的数（本题的x）
        # 零点就是本题的解
        # 求切线和x轴的交点作为下一个判断的点
        # 初始化的点设为c是为了不要找到负轴的解
        # y0’ = 2X0
        # y - y0 = 2X0(X-X0)
        # y=0, x = X0-y0/(2X0), y0=x0^2-c
        # x = x0/2 +c/(2X0), 零点，作为下一轮的x0
        if x==0:
            return 0
        x0 = x
        pre = inf
        while abs(pre-x0)>1e-7:
            pre = x0
            x0 = x0/2 + x/(2*x0)
        return int(x0)


执行用时：32 ms, 在所有 Python3 提交中击败了98.82%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.25%的用户
