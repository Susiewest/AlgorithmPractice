class Solution:
    def isValid(self, s: str) -> bool:
        #如果定义stack=[] “）”pop的时候是空
        #如果定义stack=[n]会报错
        stack=['n']
        brackets={'(':')','[':']','{':'}','n':'n'}
        for i in range(len(s)):
            if s[i] in brackets.keys():
                stack.append(s[i])
            elif brackets[stack.pop()]!=s[i]:
                return False
        #return len(stack) == 1
        return True if len(stack)==1 else False
'''执行结果：通过
执行用时：
36 ms, 在所有 Python3 提交中击败了91.32%的用户
内存消耗：
13.7 MB, 在所有 Python3 提交中击败了5.22%的用户'''
