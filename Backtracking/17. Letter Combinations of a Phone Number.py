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
不递归的做法！
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combination=[]
        if not digits:
            return combination
        combination=['']
        tmp=''
        chart=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        for i in digits:
            for _ in range(len(combination)): #对每个新i 当前comb里面的所有都是上层的节点
                tmp=combination.pop(0)
                for j in chart[ord(i)-50]: #ascii码-48转为数字，再-2转为从0开始
                    combination.append(tmp+j)
        return combination

执行用时：52 ms, 在所有 Python3 提交中击败了6.45%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了30.91%的用户

#如果把自己定义的函数不以并列的形式def 而是包含的方式def 就不一定要return一个值
#而且也不需要把其他用到的变量传递进去
#妙呀

本来觉得回溯法不需要设置depth，但写着写着发现不设置的话，无法知道走到digits的第几个位置了
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.combination=[]
        if not digits:
            return self.combination       
        path=''
        chart=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        def backtrack(path, depth):
            if len(path)==len(digits):
                self.combination.append(path)
                return
            for letter in chart[int(digits[depth])-2]:
                backtrack(path+letter, depth+1)
        backtrack('',0)
        return self.combination
执行用时：40 ms, 在所有 Python3 提交中击败了62.12%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了9.78%的用户
