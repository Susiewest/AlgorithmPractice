好多坑啊 发现自己还会把=写成== 呜呜 我好笨好菜
class Solution:
    def calculate(self, s: str) -> int:
        #乘除先算 减号化为+负数 最后求和
        #设置符号位 每遇到一个非数字的 证明前面这段是一个完整数字了，加上符号位入栈
        #再将符号为换为当前
        def cal(s):
            sign = '+'
            stack = []
            num = 0
            for i in range(len(s)):
                if s[i].isdigit():
                    #不写括号会报错 优先级会先执行+号
                    #TypeError: unsupported operand type(s) for -: 'str' and 'str' 不能像c++一样写‘5’-‘0’转化为int 5
                    num = num*10+int(s[i])
                if s[i]=='(':
                    num = cal(s[i+1:])
                if s[i]==')':
                    return sum(stack)
                #if not s[i].isdigit() and s[i]!=' ':
                #这么写不行 最后一个数字会无法参与计算
                if (not s[i].isdigit() and s[i]!=' ') or i==len(s)-1:
                    #要记住sign不是下一个数字的sign 是已经计算出的num的sign
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        #stack.append(stack[-1]*num) 不是append 是覆盖stack[-1]
                        stack[-1] = stack[-1]*num
                    elif sign == '/':
                        #stack.append(stack[-1]//num)
                        #stack[-1] = stack[-1]//num 一般的，0.5这种末尾是5的小数，四舍五入取整应进位。这个进位的意思是：-0.5 → -1；0.5 → 1.即正负情况不同，都向着远离0，使得绝对值更大的方向进位
                        #题目要求向0取整
                        stack[-1] = int(stack[-1]/num)
                    sign = s[i]
                    num = 0
            return sum(stack)
        return cal(s)
        
执行用时：108 ms, 在所有 Python3 提交中击败了67.96%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了65.20%的用户
