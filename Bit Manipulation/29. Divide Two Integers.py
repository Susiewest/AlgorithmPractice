#将除法转换为减法 为了在数字很大的情况不超时 减去的数会翻倍
#为了不让翻倍影响小数字计算 只要原除数本身不大于被除数 就继续置翻倍的除数变量为原除数来计算最后几步（14行
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #异或操作 ^ 可以判断俩数字是否异号
        if dividend^divisor>=0:
            sign=0
        else:
            sign=1
        result=0
        dividend=abs(dividend)
        divisor=abs(divisor)
        while(dividend>=divisor):
            tmp,time=divisor,1
            while(dividend>=tmp):
                dividend-=tmp
                result+=time
                tmp<<=1 #除数翻倍 我人傻了 一开始写的tmp<<1 一直超时 原来直接那么写 位移后的并不会存在变量里 所以加个‘=’
                time<<=1
        if sign:
            result=-result
        return min(max(-2**31, result), 2**31-1)
        
'''执行用时：
40 ms, 在所有 Python3 提交中击败了88.44%的用户
内存消耗：
13.3 MB, 在所有 Python3 提交中击败了75.36%的用户'''
