#此代码有问题 我将二进制转为十进制进行计算 由于int的长度等限制，对于无敌长的极端测试用例无法通过 看来要用字符串处理 有空了再写
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # append+reverse 好像会比insert省时间？
        if a=='0' and b=='0':
            return '0'
        integer_a = 0
        integer_b = 0
        result = ''
        for i in range(len(a)):
            integer_a += int(a[i]) * 2 ** (len(a) - i - 1)
        for i in range(len(b)):
            integer_b += int(b[i]) * 2 ** (len(b) - i - 1)
        add = integer_a + integer_b
        while (add != 0):
            result+=str(add % 2)
            add=int(add/2)
        return result[::-1]

