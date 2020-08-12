class Solution:
    def romanToInt(self, s: str) -> int:
    #只有在遇到特殊情况时，两个字符中左边的字符小于右边的字符，且等于右边的字符代表的数减左边字符代表的数。*/
        #RomantoInt={I:1,V:5,X:10,L:50,C:100,D:500,M:1000}
        #会说V未定义
        
        RomantoInt={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        for i in range(len(s)- 1):
            if RomantoInt[s[i]]<RomantoInt[s[i+1]]:
                #这里要注意是字典对应的数字比大小 不是罗马字母比大小
                sum-=RomantoInt[s[i]]
            else:
                sum+=RomantoInt[s[i]]
        #疑问：for i in range（len-1）最后一个循环执行完 还会i++吗
        sum+=RomantoInt[s[-1]]
        return sum

'''执行结果：通过

执行用时：60 ms, 在所有 Python3 提交中击败了72.97%的用户
内存消耗：
13.6 MB, 在所有 Python3 提交中击败了6.45%的用户'''
