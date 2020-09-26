#测试用例1074/1079 做的想吐 nmgb
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        remove_whitespace=str.lstrip(' ')
        if remove_whitespace is '' or remove_whitespace[0].isalpha():
            return 0
        if '+' in remove_whitespace and '-' in remove_whitespace and remove_whitespace[0]!='-' and remove_whitespace[0]!='+':
            return 0
        character=re.findall('[\d,\.,a-zA-Z,\s]',remove_whitespace)
        character=''.join(character)
        character= re.split('[\s,\.,a-zA-Z]', character)[0]
        num=int(character) if character!='' else 0
        flag=True
        if remove_whitespace[0]=='-':
            flag=False
        if flag==False:
            if -num>=-2**31:
                return -num
            else:
                return -2**31
        elif flag:
            if num<=2**31-1:
                return num
            else:
                return 2**31-1

#看了看答案 原来正则表达式可以设置强制从开头匹配。。。哎 我好笨
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        remove_whitespace=str.lstrip(' ')
        character=re.findall('^[\+\-]?\d+',remove_whitespace)
        num=int(character[0]) if len(character)!=0 else 0
        if num==0: return 0
        flag=True
        if remove_whitespace[0]=='-':
            flag=False
        if flag==False:
            if num>=-2**31:
                return num
            else:
                return -2**31
        elif flag:
            if num<=2**31-1:
                return num
            else:
                return 2**31-1

'''执行用时：
44 ms, 在所有 Python3 提交中击败了79.91%的用户
内存消耗：
13.4 MB, 在所有 Python3 提交中击败了47.78%的用户'''

#又简单改了一下逻辑
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        remove_whitespace=str.lstrip(' ')
        character=re.findall('^[\+\-]?\d+',remove_whitespace)
        if len(character)==0:
            return 0
        num=int(character[0])
        flag=True
        if remove_whitespace[0]=='-':
            flag=False
        if flag==False:
            if num>=-2**31:
                return num
            else:
                return -2**31
        elif flag:
            if num<=2**31-1:
                return num
            else:
                return 2**31-1
        

'''执行用时：
32 ms, 在所有 Python3 提交中击败了99.45%的用户
内存消耗：
13.4 MB, 在所有 Python3 提交中击败了22.03%的用户'''

#md答案用dfa做 我吓死了 这j8题还有点深度 果然还是我太菜 有空学习一下
#一个疑问 题解在findall了以后 写了一个解包 num = int(*num) 这样对“”空测试用例也不会报错？为啥会这样 我的就要报错 因为character[0]为空 没法int
