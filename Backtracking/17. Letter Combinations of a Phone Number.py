#如果把自己定义的函数不以并列的形式def 而是包含的方式def 就不一定要return一个值
#而且也不需要把其他用到的变量传递进去
#妙呀
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combination=[]
        if not digits:
            return combination
        tmp=''
        chart=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        def dfs(tmp,layer):
            if layer==len(digits):
                combination.append(tmp)
                return 
            index=digits[layer]
            letters=chart[int(index)-2]
            for i in letters:
                dfs(tmp+i,layer+1)
        dfs('',0)
        return combination
            

            
'''执行用时：
44 ms, 在所有 Python3 提交中击败了43.88%的用户
内存消耗：
13.4 MB, 在所有 Python3 提交中击败了60.44%的用户'''
