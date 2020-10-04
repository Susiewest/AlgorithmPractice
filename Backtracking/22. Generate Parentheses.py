class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        if n==0:
            return result
        left, right=n, n
        tmp=''
        def dfs(tmp,left,right):
            if left==right and left==0:
                result.append(tmp)
                return
            elif left>right: #左括号剩下的比右括号多 剪枝情况
                return
            if left>0:
                dfs(tmp+'(',left-1,right)
            if right>0:
                dfs(tmp+')',left,right-1)
        #啊忘了调函数
        dfs('',n,n)
        return result
        
'''执行用时：
36 ms, 在所有 Python3 提交中击败了94.24%的用户
内存消耗：
13.5 MB, 在所有 Python3 提交中击败了59.94%的用户'''
